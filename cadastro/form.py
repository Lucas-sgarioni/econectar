from django import forms
from cadastro.models import Cadastro, Entrar

class CadastrarForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Cadastro
        fields = [
            'nome', 
            'email',
            'telefone',
            'endereco',
            'senha',
        ]

class EntrarForm(forms.ModelForm):

    class Meta:
        model = Entrar
        fields = [
            'email',
            'senha',
        ]