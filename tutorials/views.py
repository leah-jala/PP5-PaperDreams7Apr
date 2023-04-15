from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import TutorialCategory, Tutorial, TutorialPost
from .forms import TutorialForm


class CreateTutorialView(CreateView):
    """
    Renders a view to allow a superuse to create a 
    tutorial
    """
    template_name = 'tutorials/add_tutorial.html'
    model: Tutorial
    form_class = TutorialForm
    success_url = '/tutorials/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateTutorialView, self).form_valid(form)


def tutorial_list(request):
    """ A view to return the main tutorials page """

    return render(request, 'tutorials/tutorial_list.html')
