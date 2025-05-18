"""
URL configuration for econectar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from base.views import inicio
from cadastro.views import cadastrar, entrar
from agendamento.views import agendamento, lista_agendamentos
from reciclagem.views import reciclagem

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='home'),
    path('cadastro/', cadastrar, name='cadastro'),
    path('accounts/login/', entrar, name='login'),
    path('agendamento/', agendamento, name='agendamento'),
    path('reciclagem/', reciclagem, name='reciclagem'),
    path('agendamentos/', lista_agendamentos, name='agendamentos')
]
