from django.apps import AppConfig


class LearnConfig(AppConfig):
    """
    AppConfig for the tutorials app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tutorials'
