from django.contrib.auth.forms import UserCreationForm
from cadastro.models import Cadastro

class CadastrarForm(UserCreationForm):
    class Meta:
        model = Cadastro
        fields = [
            'nome', 
            'email',
            'telefone',
            'endereco',
            'username',
            'password',
        ]
