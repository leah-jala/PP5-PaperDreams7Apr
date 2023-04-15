from django.urls import path
from . import views

urlpatterns = [
    path('tutorials/', views.tutorials, name='tutorials'),
]
