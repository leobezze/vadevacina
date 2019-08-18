from django.shortcuts import render
from .models import Posto, Vacina

def posto_list(request):
    context = {
        'posto_list': Posto.objects.all()
    }
    return render(request, 'postos/posto_list.html', context)

def posto(request, slug):
    posto = Posto.objects.get(slug=slug)
    context = {
        'listagem_de_postos': posto
    }

    return render(request, 'postos/posto.html', context)


def vacina(request):
    context = {
        'vacina': Vacina.objects.all()
    }
    return render(request, 'postos/vacinas/vacina.html', context)