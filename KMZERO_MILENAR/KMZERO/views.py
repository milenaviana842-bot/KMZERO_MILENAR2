from django.shortcuts import render

def login_view(request):
    return render(request, 'KMZERO/login.html')

def home(request):
    return render(request, 'KMZERO/home.html')

def cadastro(request):
    return render(request, 'KMZERO/cadastro.html')

def eventocadastrar(request):
    return render(request, 'KMZERO/eventocadastrar.html')

def eventolistar(request):
    return render(request, 'KMZERO/eventolistar.html')

def listar(request):
    atletas = [
        {"id": 1, "nome": "Roberto Franco", "categoria": "Master", "evento": "Corrida do Sol"},
        {"id": 2, "nome": "Ana Lima", "categoria": "Elite", "evento": "Maratona Amazônia"},
        {"id": 3, "nome": "Carlos Silva", "categoria": "Iniciante", "evento": "Corrida Noturna"},
        {"id": 4, "nome": "Juliana Souza", "categoria": "Elite", "evento": "Meia Maratona Belém"},
        {"id": 5, "nome": "Marcos Oliveira", "categoria": "Master", "evento": "Corrida das Águas"},
        {"id": 6, "nome": "Fernanda Costa", "categoria": "Iniciante", "evento": "Desafio Porto de Moz"},
        {"id": 7, "nome": "Pedro Henrique", "categoria": "Elite", "evento": "Maratona Amazônia"},
        {"id": 8, "nome": "Camila Rocha", "categoria": "Master", "evento": "Corrida do Sol"},
        {"id": 9, "nome": "Lucas Almeida", "categoria": "Iniciante", "evento": "Corrida Noturna"},
        {"id": 10, "nome": "Patrícia Gomes", "categoria": "Elite", "evento": "Meia Maratona Belém"},
        {"id": 11, "nome": "Rafael Santos", "categoria": "Master", "evento": "Desafio Porto de Moz"},
        {"id": 12, "nome": "Beatriz Martins", "categoria": "Iniciante", "evento": "Corrida das Águas"},
        {"id": 13, "nome": "Gustavo Ribeiro", "categoria": "Elite", "evento": "Corrida do Sol"},
    ]

    return render(request, 'KMZERO/listar.html', {'atletas': atletas})