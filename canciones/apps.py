from django.apps import AppConfig


class CancionesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "canciones"
    verbose_name = "Canciones"

    def ready(self):
        # Conecta la señal que crea el Perfil automáticamente
        # cada vez que se crea un usuario nuevo (registro o createsuperuser).
        import canciones.signals  # noqa: F401
