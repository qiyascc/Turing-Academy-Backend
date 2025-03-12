#!/bin/bash

echo -e "\e[1;36m"
cat << "EOF"
                 ___ ___  
                / __/ __|
               | (_| (__   
                \___\___|   

    You don't have to do anything, 
            just sit back,
        sit down and watch. 
     I'll just ask a few questions 
        here and there. :D
EOF
echo -e "\e[0m"

echo -e "\e[1;32m🚀 The magnificent installation begins... Sit back and watch.\e[0m"
sleep 2

APP_NAME="turing-back-cc"
DOMAIN_PROMPT="🌍 Please enter your domain address (e.g., example.com):"
CURRENT_USER=$(whoami)
CURRENT_DIR=$(pwd)

echo -e "\e[1;34m🔄 First, we update the system.\e[0m"
sudo apt-get update -y
sudo apt-get upgrade -y
echo -e "\e[1;32m✅ The update is complete, now we will move on to installing the necessary packages.\e[0m"
sleep 2

echo -e "\e[1;34m📦 Installing necessary packages...\e[0m"
sudo apt install python3-venv python3-dev libpq-dev postgresql postgresql-contrib nginx curl -y
echo -e "\e[1;32m✅ Packages installed successfully.\e[0m"
sleep 2

echo -e "\e[1;34m🔧 Setting up the virtual environment and installing dependencies...\e[0m"
if command -v poetry &> /dev/null; then
    echo -e "\e[1;32m🐍 Poetry is installed. Using Poetry for virtual environment setup.\e[0m"
    poetry shell
    poetry install
else
    echo -e "\e[1;33m❌ Poetry not found. Falling back to venv and requirements.txt.\e[0m"
    python -m venv venv
    source venv/bin/activate
    if [ -f "requirements.txt" ]; then
        pip install -r requirements.txt
    else
        echo -e "\e[1;31m❌ requirements.txt not found. Please ensure dependencies are installed manually.\e[0m"
        exit 1
    fi
fi
echo -e "\e[1;32m✅ Virtual environment and dependencies set up successfully.\e[0m"
sleep 2

echo -e "\e[1;34m🗃️ Running database migrations...\e[0m"
python manage.py makemigrations
python manage.py migrate
echo -e "\e[1;32m✅ Database migrations completed.\e[0m"
sleep 2

echo -e "\e[1;34m👑 Creating an admin user to manage the project...\e[0m"
python manage.py createsuperuser
echo -e "\e[1;32m✅ Admin user created successfully.\e[0m"
sleep 2

echo -e "\e[1;34m📂 Collecting static files...\e[0m"
python manage.py collectstatic
echo -e "\e[1;32m✅ Static files collected successfully.\e[0m"
sleep 2

echo -e "\e[1;34m${DOMAIN_PROMPT}\e[0m"
read -r domain

if command -v poetry &> /dev/null; then
    GUNICORN_PATH=$(find /etc/poetry -type d -name "${APP_NAME}*" -exec find {} -name "gunicorn" -type f \; | head -n 1)
else
    GUNICORN_PATH=$(find venv -type d -name "bin" -exec find {} -name "gunicorn" -type f \; | head -n 1)
fi

if [ -z "$GUNICORN_PATH" ]; then
    echo -e "\e[1;31m❌ Gunicorn not found. Please check manually.\e[0m"
    exit 1
fi

SOCKET_FILE_CONTENT="[Unit]
Description=${APP_NAME} socket

[Socket]
ListenStream=/run/${APP_NAME}.sock

[Install]
WantedBy=sockets.target"

SERVICE_FILE_CONTENT="[Unit]
Description=gunicorn daemon
Requires=${APP_NAME}.socket
After=network.target

[Service]
User=${CURRENT_USER}
Group=www-data
WorkingDirectory=${CURRENT_DIR}
ExecStart=${GUNICORN_PATH} \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/${APP_NAME}.sock \
          turing_back.wsgi:application

[Install]
WantedBy=multi-user.target"

echo -e "\e[1;34m🔌 Creating systemd socket file...\e[0m"
sudo bash -c "echo '${SOCKET_FILE_CONTENT}' > /etc/systemd/system/${APP_NAME}.socket"
echo -e "\e[1;32m✅ Systemd socket file created successfully.\e[0m"
sleep 2

echo -e "\e[1;34m⚙️ Creating systemd service file...\e[0m"
sudo bash -c "echo '${SERVICE_FILE_CONTENT}' > /etc/systemd/system/${APP_NAME}.service"
echo -e "\e[1;32m✅ Systemd service file created successfully.\e[0m"
sleep 2

echo -e "\e[1;34m🚀 Starting and enabling the socket...\e[0m"
sudo systemctl start ${APP_NAME}.socket
sudo systemctl enable ${APP_NAME}.socket
echo -e "\e[1;32m✅ Socket started and enabled successfully.\e[0m"
sleep 2

NGINX_CONFIG_CONTENT="server {
    listen 80;
    server_name ${domain};

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root ${CURRENT_DIR};
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/${APP_NAME}.sock;
    }
}"

echo -e "\e[1;34m🌐 Creating Nginx configuration file...\e[0m"
sudo bash -c "echo '${NGINX_CONFIG_CONTENT}' > /etc/nginx/sites-available/${APP_NAME}"
echo -e "\e[1;32m✅ Nginx configuration file created successfully.\e[0m"
sleep 2

echo -e "\e[1;34m🔗 Enabling the Nginx site...\e[0m"
sudo ln -s /etc/nginx/sites-available/${APP_NAME} /etc/nginx/sites-enabled
echo -e "\e[1;32m✅ Nginx site enabled successfully.\e[0m"
sleep 2

echo -e "\e[1;34m🔄 Restarting Nginx...\e[0m"
sudo systemctl restart nginx
echo -e "\e[1;32m✅ Nginx restarted successfully.\e[0m"
sleep 2

echo -e "\e[1;34m🔥 Allowing Nginx through the firewall...\e[0m"
sudo ufw allow 'Nginx Full'
echo -e "\e[1;32m✅ Nginx allowed through the firewall successfully.\e[0m"
sleep 2

echo -e "\e[1;33m🔐 Do you want to install Certbot and set up SSL for your domain?\e[0m"
echo -e "\e[1;36m1: Yes, install Certbot and set up SSL.\e[0m"
echo -e "\e[1;36m2: No, skip SSL setup for now.\e[0m"
read -r certbot_choice

if [ "$certbot_choice" = "1" ]; then
    echo -e "\e[1;34m🔧 Installing Certbot and setting up SSL...\e[0m"
    sudo apt install certbot python3-certbot-nginx -y
    echo -e "\e[1;32m✅ Certbot installed successfully.\e[0m"

    echo -e "\e[1;34m🔒 Obtaining SSL certificate for ${domain}...\e[0m"
    sudo certbot --nginx -d "${domain}"
    echo -e "\e[1;32m✅ SSL certificate obtained successfully.\e[0m"

    echo -e "\e[1;34m⏲️ Checking Certbot timer status...\e[0m"
    sudo systemctl status certbot.timer
    echo -e "\e[1;32m✅ Certbot timer status checked.\e[0m"

    echo -e "\e[1;34m🔄 Testing Certbot auto-renewal...\e[0m"
    sudo certbot renew --dry-run
    echo -e "\e[1;32m✅ Certbot auto-renewal test completed.\e[0m"

    echo -e "\e[1;32m🎉 SSL setup completed successfully!\e[0m"
elif [ "$certbot_choice" = "2" ]; then
    echo -e "\e[1;33m🚫 SSL setup skipped. You can manually set it up later using 'sudo certbot --nginx -d ${domain}'.\e[0m"
else
    echo -e "\e[1;31m❌ Invalid choice! SSL setup skipped.\e[0m"
fi

echo -e "\e[1;35m🎉 All setup completed! Your application is now live at: http://${domain}\e[0m"
if [ "$certbot_choice" = "1" ]; then
    echo -e "\e[1;35m🔒 SSL is active! Your application is also available at: https://${domain}\e[0m"
fi