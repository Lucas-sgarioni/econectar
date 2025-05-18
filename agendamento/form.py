from django import forms
from agendamento.models import Agendamento

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = [
            'nome',
            'email',
            'endereco',
            'data',
            'hora',
            'observacao'
        ]