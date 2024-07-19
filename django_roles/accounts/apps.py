from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "accounts"
    verbose_name = 'perfiles'

    def ready(self) -> None:
        import accounts.signals
        
    