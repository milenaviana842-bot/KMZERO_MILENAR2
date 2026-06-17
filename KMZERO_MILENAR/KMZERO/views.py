from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from .models import Atleta
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def listar(request):
    return render(request, 'KMZERO/listar.html')

def cadastro(request):
    if request.method == 'POST':

        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['senha']

        cpf = request.POST['cpf']
        telefone = request.POST['telefone']
        endereco = request.POST['endereco']
        cidade = request.POST['cidade']
        uf = request.POST['uf']
        cep = request.POST['cep']
        data_nascimento = request.POST['datanascimento']
        foto = request.FILES.get('foto')

        user = User.objects.create_user(
            username=email,
            email=email,
            password=senha,
            first_name=nome
        )

        grupo = Group.objects.get(name='ATLETA')
        user.groups.add(grupo)

        Atleta.objects.create(
            user=user,
            cpf=cpf,
            telefone=telefone,
            endereco=endereco,
            cidade=cidade,
            uf=uf,
            cep=cep,
            data_nascimento=data_nascimento,
            foto=foto
        )

        return redirect('KMZERO:login')

    return render(request, 'KMZERO/cadastro.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']

        user = authenticate(request, username=email, password=senha)

        if user is not None:
            login(request, user)
            return redirect('KMZERO:home')
        else:
            return render(request, 'KMZERO/login.html', {
                'erro': 'Login inválido'
            })

    return render(request, 'KMZERO/login.html')


@login_required
def home(request):
    return render(request, 'KMZERO/home.html')

def evento_cadastrar(request):
    return render(request, 'KMZERO/eventocadastrar.html')

def eventolistar(request):
    return render(request, 'KMZERO/eventolistar.html')

def listar(request):
    return render(request, 'KMZERO/listar.html')