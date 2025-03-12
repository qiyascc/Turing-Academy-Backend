import requests
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Contact

def send_telegram_message(message):
    TELEGRAM_BOT_TOKEN = getattr(settings, "TELEGRAM_BOT_TOKEN", None)
    CHAT_ID = getattr(settings, "CHAT_ID", None)

    if not TELEGRAM_BOT_TOKEN or not CHAT_ID:
        print("TELEGRAM_BOT_TOKEN or CHAT_ID not found")
        return

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=data)

@receiver(post_save, sender=Contact)
def send_contact_to_telegram(sender, instance, created, **kwargs):
    if created:
        specialities = ", ".join(instance.speciality_name) if instance.speciality_name else "None"

        message = (
            f"📩 New Contact\n\n"
            f"👤 Name: {instance.name}\n"
            f"👥 Surname: {instance.surname}\n"
            f"📧 Email: {instance.email}\n"
            f"📞 Phone: {instance.phone}\n"
            f"🎯 Specialities: {specialities}\n"
        )
        send_telegram_message(message)