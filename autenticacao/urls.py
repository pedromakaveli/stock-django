from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login_page, name="login"),
    path('cadastro', views.cadastro, name="cadastro"),
    path('logout', views.logout_view, name="logout")
]
