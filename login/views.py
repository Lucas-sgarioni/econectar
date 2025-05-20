from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from login.form import EntrarForm

def entrar(request):
    contexto = {'sucesso': False}
    form = EntrarForm(request, data=request.POST or None)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next') or 'home'
            return redirect(next_url)
        else:
            print('Usuário ou senha inválidos!')
    contexto['form'] = form
    return render(request, 'registration/login.html', contexto)