from django.shortcuts import render
from cadastro.form import CadastrarForm, EntrarForm
from cadastro.models import Cadastro

def cadastrar(request):
    contexto = {'sucesso' : False}
    forms_cadastro = CadastrarForm(request.POST or None)
    if forms_cadastro.is_valid():
        forms_cadastro.save()
        contexto['sucesso'] = True
    contexto['form'] = forms_cadastro
    return render(request, 'cadastro.html', contexto)

def entrar(request):
    contexto = {'sucesso' : False}
    forms_login = EntrarForm(request.POST or None)
    if forms_login.is_valid():
        forms_login.save()
        contexto['sucesso'] = True
    contexto['form'] = forms_login
    return render(request, 'login.html', contexto)