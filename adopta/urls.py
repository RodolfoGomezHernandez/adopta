from django.urls import path
from . import views

urlpatterns = [
    # La ruta raíz ('') se asigna a la vista 'home'.
    path('', views.home, name='home'),
    path('contacto/', views.contacto, name='contacto'),
]