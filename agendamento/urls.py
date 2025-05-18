from django.urls import path
from agendamento.views import agendamento, lista_agendamentos

urlpatterns = [
    path('agendamento/', agendamento, name='agendamento'),
    path('agendamentos/', lista_agendamentos, name='lista_agendamentos'),
]