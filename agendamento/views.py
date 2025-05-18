from django.shortcuts import render
from agendamento.form import AgendamentoForm
from agendamento.models import Agendamento
from django.contrib.auth.decorators import login_required

@login_required
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

@login_required
def lista_agendamentos(request):
    agendamentos = Agendamento.objects.all().order_by('-data', '-hora')
    return render(request, 'lista/lista_agendamentos.html', {
        'agendamentos': agendamentos
    })