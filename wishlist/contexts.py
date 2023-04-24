from .models import Wishlist

def wishlist(request):
    """ Add the wishlist to the context if the user is authenticated """
    wishlist = None
    if request.user.is_authenticated:
        wishlist, _ = Wishlist.objects.get_or_create(user=request.user)
    return {'wishlist': wishlist}
