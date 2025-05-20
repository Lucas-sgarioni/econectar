from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from cadastro.models import Cadastro

class CadastroAdmin(UserAdmin):
    model = Cadastro
    fieldsets = UserAdmin.fieldsets + (
        ('Informações adicionais', {
            'fields': ('nome', 'telefone', 'endereco'),
        }),
    )

admin.site.register(Cadastro, CadastroAdmin)