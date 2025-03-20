from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('criar_produto', views.criar_produto, name="criar_produto"),
    path('criar_marca', views.criar_marca, name="criar_marca"),
    path('marcas', views.marcas, name="marcas")
]
