from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # Assurez-vous que le nom de la vue est 'home'
    path('projets/<int:pk>/', views.project_detail, name='project_detail'), # Nouvelle URL pour les détails de projet
]