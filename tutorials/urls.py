from django.urls import path
from .views import (
    CreateTutorialView, tutorial_list, TutorialDetailView,
    CreateTutorialPostView, UserTutorialsView, UpdateTutorialView,
    UpdateTutorialPostView, DeleteTutorialPostView, DeleteTutorialView
)

urlpatterns = [
    path(
        'tutorials/add/',
        CreateTutorialView.as_view(),
        name='add_tutorial'),
    path(
        'tutorials/<int:tutorial_pk>/add_post/',
        CreateTutorialPostView.as_view(),
        name='add_tutorial_post'),
    path(
        'tutorials/<int:pk>/edit/',
        UpdateTutorialView.as_view(),
        name='edit_tutorial'),
    path(
        'tutorials/<int:pk>/delete/',
        DeleteTutorialView.as_view(),
        name='delete_tutorial'),
    path(
        'tutorials/',
        tutorial_list,
        name='tutorial_list'),
    path(
        'tutorials/<int:pk>/',
        TutorialDetailView.as_view(),
        name='tutorial_detail'),
    path(
        'tutorials/<int:pk>/edit_post/',
        UpdateTutorialPostView.as_view(),
        name='edit_tutorial_post'),
    path(
        'tutorials/<int:pk>/delete_post/',
        DeleteTutorialPostView.as_view(),
        name='delete_tutorial_post'),
    path(
        'user_tutorials/',
        UserTutorialsView.as_view(),
        name='user_tutorials'),
]
