from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('lista_produtos', views.index, name="index"),
    path('criar_produto', views.criar_produto, name="criar_produto"),
    path('atualizar_produto/<id>', views.atualizar_produto, name="atualizar_produto"),
    path('atualizar_marca/<id>', views.atualizar_marca, name="atualizar_marca"),
    path('atualizar_tipo/<id>', views.atualizar_tipo, name="atualizar_tipo"),
    
    path('criar_marca', views.criar_marca, name="criar_marca"),
    path('criar_tipo', views.criar_tipo, name="criar_tipo"),
    path('categorias', views.categorias, name="categorias"),
    path('deletar_marca/<id>', views.deletar_marca, name="deletar_marca"),
    path('deletar_tipo/<id>', views.deletar_tipo, name="deletar_tipo"),
    path('marcas', views.marcas, name="marcas")
]
