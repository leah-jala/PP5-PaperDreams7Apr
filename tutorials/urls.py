from django.urls import path
from .views import (
    CreateTutorialView, tutorial_list, TutorialDetailView,
    CreateTutorialPostView, UserTutorialsView, UpdateTutorialView,
    UpdateTutorialPostView, DeleteTutorialPostView, DeleteTutorialView
)

urlpatterns = [

    path(
        'add_tutorial/',
        CreateTutorialView.as_view(),
        name='add_tutorial'),
    path(
        'add_tutorial_post/',
        CreateTutorialView.as_view(),
        name='add_tutorial_post'),
    path(
        'tutorial_list/',
        tutorial_list,
        name='tutorial_list'),
    path(
        'tutorials/<int:pk>/',
        TutorialDetailView.as_view(),
        name='tutorial_detail'),
    path(
        'tutorials/<int:tutorial_pk>/add_tutorial_post/',
        CreateTutorialPostView.as_view(),
        name='add_tutorial_post'),
    path(
        'user_tutorials/',
        UserTutorialsView.as_view(),
        name='user_tutorials'),
    path(
        'edit_tutorials/<int:pk>/',
        UpdateTutorialView.as_view(),
        name='edit_tutorial'),
    path(
        'edit_tutorial_post/<int:pk>/',
        UpdateTutorialPostView.as_view(),
        name='edit_tutorial_post'),
    path(
        'delete_tutorial/<int:pk>/',
        DeleteTutorialView.as_view(),
        name='delete_tutorial'),
    path(
        'delete_tutorial_post/<int:pk>/',
        DeleteTutorialPostView.as_view(),
        name='delete_tutorial_post'),
]
