from django import forms
from login.models import Entrar

class EntrarForm(forms.ModelForm):

    class Meta:
        model = Entrar
        fields = [
            'username',
            'password',
        ]