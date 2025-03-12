from goodconf import GoodConf
import os


class Settings(GoodConf):
    debug: bool = True
    secret_key: str = "abc"
    telegram_contact_admin: str = "5187014948"
    telegram_bot_token: str = "5570070747:AAFrcqQ9Kp1nEl9hPz6QKnuH2fLRZGLigLI"

    class Config:
        env_prefix = "turing_back_"


config = Settings()
config.load()
