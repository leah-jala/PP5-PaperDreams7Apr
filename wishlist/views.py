from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Wishlist


@login_required
def view_wishlist(request):
    """ A view to return the wishlist page """
    wishlist, _ = Wishlist.objects.get_or_create(user=request.user)
    context = {
        'wishlist': wishlist,
    }
    return render(request, 'wishlist/view_wishlist.html', context)


@login_required
def add_to_wishlist(request, item_id):
    """ Add a product to the wishlist """
    product = get_object_or_404(Product, pk=item_id)
    wishlist, _ = Wishlist.objects.get_or_create(user=request.user)
    wishlist.products.add(product)
    return redirect(reverse('view_wishlist'))


@login_required
def remove_from_wishlist(request, item_id):
    """ Remove a product from the wishlist """
    product = get_object_or_404(Product, pk=item_id)
    wishlist, _ = Wishlist.objects.get_or_create(user=request.user)
    wishlist.products.remove(product)
    return redirect(reverse('view_wishlist'))
