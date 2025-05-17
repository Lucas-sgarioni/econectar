from django.db import models

class Cadastro(models.Model):
    nome = models.CharField(verbose_name='Nome', max_length=70)
    email = models.EmailField(verbose_name='E-mail')
    telefone = models.CharField(verbose_name='Telefone', max_length=9)
    endereco = models.CharField(verbose_name='Endereço')
    senha = models.CharField(verbose_name='Senha')


    criado_em = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)

