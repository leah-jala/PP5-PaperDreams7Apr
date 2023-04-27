from django.shortcuts import render


def about(request):
    """ Render About page """
    return render(request, 'pages/about.html')


def shipping_returns(request):
    """ Render Delivery and Returns page """
    return render(request, 'pages/shipping_returns.html')


def privacy(request):
    """ Render Privacy page """
    return render(request, 'pages/privacy.html')
