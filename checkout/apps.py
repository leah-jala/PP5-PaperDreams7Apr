from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """
    Sets the default auto field and app name
    for the checkout app and imports the signals
    module when the app is ready.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    def ready(self):
        import checkout.signals
