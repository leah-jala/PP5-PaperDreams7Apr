from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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

    # Check if the item is already in the bag
    bag = request.session.get('bag', {})
    if str(item_id) in bag:
        messages.info(
            request, (
                'This item is already in your bag! '
                'Remove it from your bag, then add it '
                'to your wishlist if you are not '
                'ready to buy now.'
            )
        )
    else:
        wishlist.products.add(product)
        messages.success(request, 'Added to wishlist!')
    # Redirect the user back to the current page
    return redirect(request.META.get('HTTP_REFERER', 'home'))


@login_required
def remove_from_wishlist(request, item_id):
    """ Remove a product from the wishlist """
    product = get_object_or_404(Product, pk=item_id)
    wishlist, _ = Wishlist.objects.get_or_create(user=request.user)
    wishlist.products.remove(product)
    messages.success(request, 'Removed from wishlist!')
    return redirect(reverse('view_wishlist'))
