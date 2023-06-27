from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

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
        print(email, senha)
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)

            if user is not None:
                auth.login(request, user)
                print('Login realizado com sucesso')
                return redirect('dashboard')
            
        print('Usuário e/ou senha inválidos')
        return redirect('login')

        return redirect('dashboard')
        

    return render(request, 'login.html')

def dashboard(request):
    return render (request, 'dashboard.html')

def logout(request):
    auth.logout(request)
    print('Você realizou o Logout')
    return redirect('index')


