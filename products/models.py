from django.db import models


class Category(models.Model):
    """
    Represents product categories in the store.

    Each category has a name and a friendly_name.
    The friendly_name is used for display purposes,
    while the name is used internally.
    """

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """
    Represents products in the store.

    Each product belongs to a category and has a unique name,
    description, price, and quantity. Products can also have
    an optional SKU, image URL, and image file.
    """

    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image_alt = models.CharField(max_length=100, null=False, blank=True)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
