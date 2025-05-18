from django.shortcuts import render
from reciclagem.models import MaterialReciclavel, PontoColeta


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