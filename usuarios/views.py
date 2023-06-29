from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

from churras.models import Prato

# Create your views here.


def cadastro(request):
    #print(f'Method: {request.method}')
    if request.method == 'POST':

        #print(f'POST: {request.POST}')
        #print("cadastrado com sucesso")
        
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['senha']
        senha2 = request.POST['senha2']

        if not nome.strip():
            print('O campo nome não pode ficar em branco')
            return redirect('cadastro')
        
        if not email.strip():
            print('O campo email não pode ficar em branco')
            return redirect('cadastro')
        
        if senha != senha2 or senha.strip() or not senha2.strip():
            print('As senhas não são iguais ou uma delas está em branco')
            redirect('cadastro')

        if User.objects.filter(email=email).exists():
            print('Email já cadastrado')
            return redirect('cadastro')
        
        if User.objects.filter(username=nome).exists():
            print('Usuario já cadastrado')
            return redirect('cadastro')
        
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        print('Usuário Cadastro com Sucesso')
        
        return redirect('login')
    
    return render(request, 'cadastro.html')

def login(request):
    if  request.method == 'POST':
        print(f'POST: {request.POST}')

        email = request.POST['email']
        senha = request.POST['senha']
        if email == "" or senha == "":
            print('Os campos e-mail e senha não podem ficar em branco')
            return redirect('login')
        #print(email, senha)
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)

            if user is not None:
                auth.login(request, user)
                print('Login realizado com sucesso')
                return redirect('dashboard')
            
        print('Usuário e/ou senha inválidos')
        return redirect('login')

    return redirect('login.html')
    #return redirect('dashboard')
        

def dashboard(request):
    if request.user.is_authenticated:
        pratos = Prato.objects.filter(publicado=True).order_by('-date_prato')
        return render (request, 'dashboard.html')

    return redirect('index')

def logout(request):
    auth.logout(request)
    print('Você realizou o Logout')
    return redirect('index')

def cria_prato(request):
    if request.method == 'POST':
        print(f'\n{request.POST["nome_prato"]}')
        nome_prato = request.POST['nome_prato']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['tempo_preparo']
        tempo_preparo = request.POST['modo_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        foto_prato = request.POST['foto_prato']
        return render(request, 'cria_prato.html')


