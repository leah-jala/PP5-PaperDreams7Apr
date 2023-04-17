from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.contrib.auth.models import User
from django.contrib import messages
from .models import TutorialCategory, Tutorial, TutorialPost
from .forms import TutorialForm, TutorialPostForm


class CreateTutorialView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """
    Renders a view to allow a superuser to create a
    tutorial
    """
    template_name = 'tutorials/add_tutorial.html'
    model = Tutorial
    form_class = TutorialForm

    def form_valid(self, form):
        """
        Set's the tutorial's user as the current user
        """
        form.instance.instructor = self.request.user
        response = super(CreateTutorialView, self).form_valid(form)
        messages.success(self.request, f'Tutorial "{self.object.title}" created successfully. Now, add tutorial posts.')
        return response

    def test_func(self):
        """
        Checks if the current user is a superuser
        """
        return self.request.user.is_superuser

    def handle_no_permission(self):
        """
        Redirects users who fail the test_func (non-superusers) to
        the login page.
        """
        return redirect(reverse_lazy('account_login'))
    
    def get_success_url(self):
        return reverse_lazy('add_tutorial_post', kwargs={'tutorial_pk': self.object.pk})


class UpdateTutorialView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    A view to edit tutorial details
    """
    model = Tutorial
    template_name = 'tutorials/edit_tutorial.html'
    form_class = TutorialForm

    def test_func(self):
        tutorial = self.get_object()
        return self.request.user == tutorial.instructor

    def handle_no_permission(self):
        return redirect(reverse_lazy('account_login'))

    def get_success_url(self):
        return reverse_lazy('tutorials/user_tutorials')


class CreateTutorialPostView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """
    Renders a view to allow a superuser to create a tutorial post
    """
    template_name = 'tutorials/add_tutorial_post.html'
    model = TutorialPost
    form_class = TutorialPostForm

    def get_form_kwargs(self):
        kwargs = super(CreateTutorialPostView, self).get_form_kwargs()
        tutorial_pk = self.kwargs.get('tutorial_pk')
        kwargs['tutorial_pk'] = tutorial_pk
        return kwargs

    def form_valid(self, form):
        """
        Sets the tutorial post's instructor as the current user and associates it with the tutorial.
        """
        form.instance.instructor = self.request.user
        tutorial_pk = self.kwargs.get('tutorial_pk')
        tutorial = get_object_or_404(Tutorial, pk=tutorial_pk)
        form.instance.tutorial = tutorial
        response = super(CreateTutorialPostView, self).form_valid(form)
        messages.success(self.request, f'Tutorial post "{self.object.title}" created successfully.')
        return response

    def test_func(self):
        """
        Checks if the current user is a superuser
        """
        return self.request.user.is_superuser

    def handle_no_permission(self):
        """
        Redirects users who fail the test_func (non-superusers) to
        the login page.
        """
        return redirect(reverse_lazy('account_login'))
    
    def get_success_url(self):
        tutorial_pk = self.kwargs['tutorial_pk']
        return reverse_lazy('tutorials:tutorial_detail', args=[tutorial_pk])


class UserTutorialsView(LoginRequiredMixin, ListView):
    """
    Renders a view to display a list of tutorials for the current user.
    """
    template_name = 'tutorials/user_tutorials.html'
    context_object_name = 'tutorials'

    def get_queryset(self):
        """
        Returns the list of tutorials for the current user.
        """
        return Tutorial.objects.filter(instructor=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tutorials_with_posts = []
        for tutorial in context['tutorials']:
            tutorial_posts = TutorialPost.objects.filter(tutorial=tutorial)
            tutorials_with_posts.append({'tutorial': tutorial, 'posts': tutorial_posts})
        context['tutorials_with_posts'] = tutorials_with_posts
        return context



def tutorial_list(request):
    """ A view to return the main tutorials page """
    tutorials = Tutorial.objects.all()
    return render(request,
                  'tutorials/tutorial_list.html',
                  {'tutorials': tutorials})


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
