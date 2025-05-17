from django.shortcuts import render
from django.urls import reverse

def inicio(request):
    dados = []
    # Cada item dado aqui gerará um quadro no template inicial.
    dados.append(
        {
            'titulo' : 'Cadastre-se aqui',
            'descricao' : 'Para criar seu cadastro e começar a reciclar!',
            'link' : reverse('cadastro')
        }
    )
    dados.append(
        {
            'titulo' : 'Agende sua coleta',
            'descricao' : 'Para encontrar a cooperativa ideal para sua reciclagem e agendar a coletar',
            'link': reverse('agendamento')
        }
    )
    dados.append(
        {
            'titulo' : 'Sua contribuição',
            'descricao' : 'Para verificar quanto você já reciclou e ajudou o meio ambiente',
            'link' : reverse('reciclagem')
        }
    )
    contexto = {
        'dados' : dados
    }
    return render(request, 'inicio.html', contexto)
