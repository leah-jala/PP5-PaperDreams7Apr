from django.urls import path
from .views import CreateTutorialView, tutorial_list

urlpatterns = [
    path('', tutorial_list, name='tutorial_list_base'),
    path('add_tutorial/', CreateTutorialView.as_view(), name='add_tutorial'),
    path('tutorial_list/', tutorial_list, name='tutorial_list'),
]
