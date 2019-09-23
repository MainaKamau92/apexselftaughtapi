from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    name = 'apexselftaught.apps.authentication'

    def ready(self):
        from .signals.profile_create import create_profile  # noqa
