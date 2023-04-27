from django.apps import AppConfig


class BagConfig(AppConfig):
    """
    Specifies the name of the 'bag' app and the 
    type of auto-generated primary key field for
    models in the app. 
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bag'
