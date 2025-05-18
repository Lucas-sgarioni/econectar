from django.shortcuts import render
from agendamento.form import AgendamentoForm
from agendamento.models import Agendamento


def agendamento(request):
    success = False
    form = AgendamentoForm(request.POST or None)
    if form.is_valid():
        form.save()
        success = True
    return render(request, 'agendamento.html', {
        'form': form,
        'success': success
    })


def lista_agendamentos(request):
    agendamentos = Agendamento.objects.all().order_by('-data', '-hora')
    return render(request, 'lista/lista_agendamentos.html', {
        'agendamentos': agendamentos
    })