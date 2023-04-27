from django.db import models
from django.conf import settings
from products.models import Product


class Wishlist(models.Model):
    """
    Wishlist model for storing the 
    customer's favourite artworks.
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}\'s Wishlist'
