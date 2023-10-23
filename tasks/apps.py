from django.apps import AppConfig


class TasksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tasks'
    def ready(self):
        import tasks.signals  # Importa las señales para que se registren    