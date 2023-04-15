from django.shortcuts import render

# Create your views here.


def tutorials(request):
    """ A view to return the index page """

    return render(request, 'learn/tutorials.html')
