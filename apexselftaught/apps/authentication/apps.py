from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    name = 'apexselftaught.apps.authentication'

    def ready(self):
        from .signal import create_related_profile  # noqa
