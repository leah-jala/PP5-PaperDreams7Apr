from django.contrib import admin
from .models import Product, Category

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    """
    Customizes the display of the model in the admin panel
    """
    list_display = (
        "sku",
        "name",
        "category",
        "price",
        "quantity",
        "image",
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    """
    Customizes the display of the model in the admin panel
    """
    list_display = (
        "friendly_name",
        "name",
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
