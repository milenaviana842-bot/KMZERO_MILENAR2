from django.urls import path
from . import views

app_name = 'KMZERO'

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('listar/', views.listar, name='listar'),
    path('evento/cadastrar/', views.evento_cadastrar, name='eventocadastrar'),
    path('evento/listar/', views.eventolistar, name='eventolistar'),
    path('login/', views.login_view, name='login'),
]