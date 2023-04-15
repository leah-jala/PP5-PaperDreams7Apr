from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, DetailView
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
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorials/tutorial_list.html', {'tutorials': tutorials})


class TutorialDetailView(DetailView):
    """
    Renders a view to display the tutorial details and 
    its related tutorial posts
    """
    model = Tutorial
    template_name = 'tutorials/tutorial_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tutorial = self.get_object()
        tutorial_posts = TutorialPost.objects.filter(tutorial=tutorial)
        context['tutorial_posts'] = tutorial_posts
        return context


