from django.urls import path
from . import views

urlpatterns = [
    path('', views.ventas_view, name='Ventas'),
    path('Clientes/', views.clientes_view, name='Clientes'),
]