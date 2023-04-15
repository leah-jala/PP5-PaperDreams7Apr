from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import TutorialCategory, Tutorial, TutorialPost




# Create your views here.

class CreateTutorialView(CreateView):
    """
    Renders a view to allow a superuse to create a 
    tutorial
    """
    template_name = learn/add_tutorial.html
    success_url = '/learn/'



def tutorials(request):
    """ A view to return the index page """

    return render(request, 'learn/index.html')
