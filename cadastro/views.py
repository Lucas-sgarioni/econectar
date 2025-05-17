from django.shortcuts import render
from cadastro.form import CadastrarForm
from cadastro.models import Cadastro

def cadastrar(request):
    contexto = {'sucesso' : False}
    forms = CadastrarForm(request.POST or None)
    if forms.is_valid():
        forms.save()
        contexto['sucesso'] = True
    contexto['form'] = forms
    return render(request, 'cadastro.html', contexto)