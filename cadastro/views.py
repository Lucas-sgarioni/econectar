from django.shortcuts import render, redirect
from cadastro.form import CadastrarForm


def cadastrar(request):

    forms_cadastro = CadastrarForm(request.POST or None)
    if forms_cadastro.is_valid():
        forms_cadastro.save()
        return redirect('login')
    else: form = CadastrarForm()

    return render(request, 'cadastro.html', {'form': form})

