from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('criar_produto', views.criar_produto, name="criar_produto"),
    path('atualizar_produto/<id>', views.atualizar_produto, name="atualizar_produto"),
    path('atualizar_marca/<id>', views.atualizar_marca, name="atualizar_marca"),
    
    path('criar_marca', views.criar_marca, name="criar_marca"),
    path('criar_tipo', views.criar_tipo, name="criar_tipo"),
    path('deletar_marca/<id>', views.deletar_marca, name="deletar_marca"),
    path('marcas', views.marcas, name="marcas")
]
