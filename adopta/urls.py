from django.urls import path
from . import views

urlpatterns = [
    # La ruta raíz ('') se asigna a la vista 'home'.
    path('', views.home, name='home'),
    path('contacto/', views.contacto, name='contacto'),
    path('adopta/', views.lista_mascotas, name='lista_mascotas'),


    # Rutas de Autenticación y Panel 
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),


    # Rutas para el CRUD de Mascotas 
    path('dashboard/mascotas/', views.mascotas_list_view, name='mascotas_list'),
    path('dashboard/mascotas/agregar/', views.mascotas_create_view, name='mascotas_create'),
    path('dashboard/mascotas/editar/<int:pk>/', views.mascotas_update_view, name='mascotas_update'),
    path('dashboard/mascotas/eliminar/<int:pk>/', views.mascotas_delete_view, name='mascotas_delete'),


    # Rutas para el CRUD de Interesados
    path('dashboard/interesados/', views.interesados_list_view, name='interesados_list'),
]