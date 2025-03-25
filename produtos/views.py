from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from produtos.models import Marca
from produtos.models import Produto
from produtos.models import Tipo

# Create your views here.

@login_required(login_url="dashboard")
def dashboard (request):
    qtd_produtos = len(Produto.objects.all())
    qtd_marcas = len(Marca.objects.all())
    qtd_categorias = len(Tipo.objects.all())
    
    return render(request, "home.html", {
        "qtd_produtos": qtd_produtos, 
        "qtd_marcas": qtd_marcas,
        "qtd_categorias": qtd_categorias
        
        } )

@login_required(login_url="login")
def index (request):
    
    produtos = Produto.objects.all()
    marcas = Marca.objects.all()
    tipos = Tipo.objects.all()
    
    usuario = request.POST.get("email")
    print(usuario)
    
    return render(request, "produtos.html", {"produtos": produtos, "marcas": marcas, "tipos": tipos})

@login_required(login_url="login")
def marcas (request):
    marcas = Marca.objects.all()
    
    return render(request, "marcas.html", {"marcas": marcas})

@login_required(login_url="login")
def deletar_marca (request, id):
    print(id)
    marca = Marca.objects.get(id=id)
    marca.delete()
    
    return redirect("marcas")

@login_required(login_url="login")
def categorias (request):
    tipos = Tipo.objects.all()
    
    return render(request, "categorias.html", {"tipos": tipos})

@login_required(login_url="login")
def atualizar_tipo (request, id):
    
    nome = request.POST.get("tipo")
    tipo = Tipo.objects.get(id=id)
    tipo.nome = nome
    
    tipo.save()
    
    return redirect ('categorias')

@login_required(login_url="login")
def deletar_tipo(request, id):
    print(id)
    tipo = Tipo.objects.get(id=id)
    tipo.delete()
    
    return redirect("categorias")

@login_required(login_url="login")
def criar_tipo (request):
    nome_tipo = request.POST.get("tipo")

    if request.method == "POST":
        tipo = Tipo(nome=nome_tipo)
        tipo.save()
        

        return redirect("categorias")

        
    if request.method == "GET":
        return render(request, "criar_tipo.html")
    
@login_required(login_url="login")
def criar_marca (request):
    
    nome = request.POST.get("nome")

    if request.method == "POST":
        marca = Marca(nome=nome)
        marca.save()
        
        return redirect("criar_marca")
        
    if request.method == "GET":
    
        return render(request, "criar_marca.html")

@login_required(login_url="login")
def atualizar_marca (request, id):
    nome = request.POST.get("nome")
    marca = Marca.objects.get(id=id)
    marca.nome = nome
    
    marca.save()
    
    return redirect ('marcas')
  
@login_required(login_url="login")
def atualizar_produto (request, id):
    nome = request.POST.get("nome")
    quantidade = request.POST.get("quantidade")
    marca_nome = request.POST.get("marca")
    tipo = request.POST.get("tipo")
    
    marca = Marca.objects.get(nome=marca_nome)
    produto = Produto.objects.get(id=id)
    
    produto.nome = nome
    produto.quantidade = quantidade
    produto.marca = marca
    produto.tipo = tipo
    
    produto.save()
    
    return redirect("index")

@login_required(login_url="login")
def criar_produto (request):
    if request.method == "GET":
        marcas = Marca.objects.all()
        tipos = Tipo.objects.all()
        
        print(tipos)
        
        return render(request, "criar_produto.html", {"marcas": marcas, "tipos": tipos})
    

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