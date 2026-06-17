from django.db import models
from django.contrib.auth.models import User

class Atleta(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=20)
    data_nascimento = models.DateField(null=True, blank=True)
    endereco = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    cep = models.CharField(max_length=10)
    foto = models.ImageField(upload_to='atletas/', null=True, blank=True)

    def __str__(self):
        return self.user.username