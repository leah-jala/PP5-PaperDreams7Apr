from django.shortcuts import (
    render, redirect, reverse,
    HttpResponse, get_object_or_404,
    )
from django.contrib import messages
from products.models import Product


# Create your views here.
def view_bag(request):
    """ A view to return the shopping bag page """
    bag = request.session.get('bag', {})
    bag_items = []

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    context = {
        'bag_items': bag_items,
    }

    return render(request, 'bag/bag.html', context)


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    available_qty = product.quantity
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    message = (f"Only {available_qty} items are "
               f"available for {product.name}.")

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        if bag[item_id] > available_qty:
            bag[item_id] = available_qty
            messages.error(request, message)
        else:
            messages.success(
                request, f'Updated {product.name} quantity to {bag[item_id]}')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if item_id in bag:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(
                request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')
    else:
        messages.error(request, f'{product.name} not found in your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
