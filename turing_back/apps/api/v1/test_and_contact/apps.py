from django.apps import AppConfig


class TestAndContactConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "turing_back.apps.api.v1.test_and_contact"

    def ready(self):
        import turing_back.apps.api.v1.test_and_contact.signals
