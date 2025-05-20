from django.db import models

class Entrar(models.Model):
    username = models.CharField(verbose_name='Usuário', max_length=20)
    password = models.CharField(verbose_name='Senha', max_length=16)

    logado_em = models.DateTimeField(verbose_name='Criado em', auto_now=True)