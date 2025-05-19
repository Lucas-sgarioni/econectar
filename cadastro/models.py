from django.db import models

class Cadastro(models.Model):
    nome = models.CharField(verbose_name='Nome completo', max_length=70)
    email = models.EmailField(verbose_name='E-mail')
    telefone = models.CharField(verbose_name='Telefone', max_length=9)
    endereco = models.CharField(verbose_name='Endereço', max_length=100)
    senha = models.CharField(verbose_name='Senha', max_length=16)


    criado_em = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)

class Entrar(models.Model):
    email = models.EmailField(verbose_name='E-mail')
    senha = models.CharField(verbose_name='Senha', max_length=16)

    logado_em = models.DateTimeField(verbose_name='Criado em', auto_now=True)