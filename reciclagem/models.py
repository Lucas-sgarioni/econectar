from django.db import models

class MaterialReciclavel(models.Model):
    nome = models.CharField('Nome', max_length=100)
    descricao = models.TextField('Descrição')

    def __str__(self):
        return self.nome

class PontoColeta(models.Model):
    nome = models.CharField('Ponto de Coleta', max_length=200)
    endereco = models.CharField('Endereço', max_length=300)
    telefone = models.CharField('Telefone', max_length=50, blank=True)

    def __str__(self):
        return self.nome