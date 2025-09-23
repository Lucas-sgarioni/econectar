from django.db import models
from django.conf import settings

class Agendamento(models.Model):
  usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Usuário', null=True, blank=True)
  nome = models.CharField(verbose_name= 'Nome Completo', max_length=70)
  email = models.EmailField(verbose_name= 'E-mail')
  endereco = models.CharField(verbose_name= 'Endereço', max_length=100)
  data = models.DateField(verbose_name= 'Data de Coleta')
  hora = models.TimeField(verbose_name= 'Hora da Coleta')
  observacao = models.TextField(verbose_name= 'Observação', max_length=500)
  

# Create your models here.
