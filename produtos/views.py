from django.shortcuts import render, redirect
from django.http import HttpResponse
from produtos.models import Marca
from produtos.models import Produto

# Create your views here.

def index (request):
    
    produtos = Produto.objects.all()
    
    return render(request, "produtos.html", {"produtos": produtos})

def marcas (request):
    marcas = Marca.objects.all()
    
    return render(request, "marcas.html", {"marcas": marcas})

def criar_marca (request):
    
    nome = request.POST.get("nome")

    if request.method == "POST":
        marca = Marca(nome=nome)
        marca.save()
        
        return redirect("criar_marca")
        
    if request.method == "GET":
    
        return render(request, "criar_marca.html")
        

def criar_produto (request):
    if request.method == "GET":
        print("condição caiu no get")
        marcas = Marca.objects.all()
        print(marcas)
    
        return render(request, "criar_produto.html", {"marcas": marcas})

    if request.method == "POST":
        nome = request.POST.get("nome")
        tipo = request.POST.get("tipo")
        marca_nome = request.POST.get("marca")
        quantidade = request.POST.get("quantidade")
        
        marca = Marca.objects.get(nome=marca_nome)
        
        produto = Produto(
            nome=nome,
            tipo=tipo,
            marca=marca,
            quantidade=quantidade
        )
        
        produto.save()
    
    return render(request, "criar_produto.html")