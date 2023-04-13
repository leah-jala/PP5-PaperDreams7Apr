from django.shortcuts import render

def about(request):
    return render(request, 'pages/about.html')

def shipping_returns(request):
    return render(request, 'pages/shipping_returns.html')

def privacy(request):
    return render(request, 'pages/privacy.html')
