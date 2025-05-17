from django import forms
from cadastro.models import Cadastro

class CadastrarForm(forms.ModelForm):

    class Meta:
        model = Cadastro
        fields = [
            'nome', 
            'email',
            'telefone',
            'endereco',
            'senha'
        ]
