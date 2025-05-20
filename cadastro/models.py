from django.db import models
from django.contrib.auth.models import AbstractUser

class Cadastro(AbstractUser):
    nome = models.CharField(verbose_name='Nome completo', max_length=70)
    email = models.EmailField(verbose_name='E-mail')
    telefone = models.CharField(verbose_name='Telefone', max_length=9)
    endereco = models.CharField(verbose_name='Endereço', max_length=100)


    criado_em = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)

