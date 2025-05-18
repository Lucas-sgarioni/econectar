from django.db import models

class Agendamento(models.Model):
  nome = models.Charfield(verbose_name= 'Nome Completo', max_length=70)
  email = models.EmailField(verbose_name= 'E-mail')
  endereco = models.CharField(verbose_name= 'Endereço', max_length=100)
  data = models.DateField(verbose_name= 'Data de Coleta')
  hora = models.TimeField(verbose_name= 'Hora da Coleta')
  observacao = models.CharFfield(verbose_name= 'Observação', max_length=999)
  

# Create your models here.
