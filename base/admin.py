from django.contrib import admin

from cadastro.models import Cadastro, Entrar

@admin.register(Cadastro)
class CadastroAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'telefone', 'endereco', 'senha']
    search_fields = ['nome', 'email']