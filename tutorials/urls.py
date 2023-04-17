from django.urls import path
from .views import CreateTutorialView, tutorial_list, TutorialDetailView

urlpatterns = [
    path(
        '',
        tutorial_list,
        name='tutorial_list_base'),
    path(
        'add_tutorial/',
        CreateTutorialView.as_view(),
        name='add_tutorial'),
    path(
        'tutorial_list/',
        tutorial_list,
        name='tutorial_list'),
    path(
        'tutorials/<int:pk>/',
        TutorialDetailView.as_view(),
        name='tutorial_detail'),
    path(
        'tutorials/<int:tutorial_pk>/add_post/',
        CreateTutorialPostView.as_view(),
        name='add_tutorial_post'),
]
