from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='Ficha Mantenimiento'), # index de las fichas
    path('nuevo/', views.guardar, name='crear_ficha'),
    
]