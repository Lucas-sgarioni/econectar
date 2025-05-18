from django.shortcuts import render
from reciclagem.models import MaterialReciclavel, PontoColeta
from django.contrib.auth.decorators import login_required

@login_required
def reciclagem(request):
    query = request.GET.get('q', '')
    # lista de pontos para autocomplete
    pontos = PontoColeta.objects.all().order_by('nome')
    results = []
    if query:
        results = MaterialReciclavel.objects.filter(nome__icontains=query)
    return render(request, 'reciclagem.html', {
        'results': results,
        'pontos': pontos,
        'query': query
    })