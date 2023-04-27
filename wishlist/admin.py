from django.contrib import admin
from .models import Wishlist


class WishlistAdmin(admin.ModelAdmin):
    """
    Django admin configuration for the Wishlist model.

    """
    list_display = ('user', 'formatted_date_added', 'product_list')
    readonly_fields = ('date_added',)

    def product_list(self, obj):
        """
        Return a comma-separated list of the products in the wishlist.
        """
        return "\n".join([p.name for p in obj.products.all()])

    product_list.short_description = "Products"

    def formatted_date_added(self, obj):
        """
        Return the date added to the wishlist in a human-readable format.
        """
        return obj.date_added.strftime("%b %d, %Y %H:%M:%S")

    formatted_date_added.short_description = "Date added"


admin.site.register(Wishlist, WishlistAdmin)
