from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from produtos import urls
# Create your views here.

def logout_view (request):
    logout(request)
    
    return redirect("login")

def login_page (request):
    if request.method == "GET":
        return render(request, "login.html")
    
    if request.method == "POST":
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        
        user = authenticate(request, username = email, password = senha)
        
        print(email, senha)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            messages.error(request, "Credenciais inválidas ou usuário não existe.")
            return redirect("login")  # Redireciona de volta ao login
        

def cadastro (request):
    
    if request.method == "GET":
        return render(request, "cadastro.html")

    if request.method == "POST":
        nome = request.POST.get("nome")
        sobrenome = request.POST.get("sobrenome")
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        
        print(nome,sobrenome,email,senha)
        
        user = User.objects.create_user(first_name=nome, username=email, password=senha)
        user.last_name = sobrenome
        user.save()
        
        return render(request, "cadastro.html")