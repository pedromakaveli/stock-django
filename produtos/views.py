from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index (request):
    return HttpResponse("Página de produtos")

def criar_produto (request):
    return HttpResponse("Página para criar produto")