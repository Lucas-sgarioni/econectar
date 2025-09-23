from django.shortcuts import render, redirect
from django.contrib.auth import login
from login.form import LoginForm

def entrar(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # Implementar "Lembrar-me"
            if not request.POST.get('remember_me'):
                request.session.set_expiry(0)  # Expira ao fechar o navegador

            next_url = request.GET.get('next') or 'home'
            return redirect(next_url)
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})