from django.shortcuts import render
from .models import Posto


def posto_list(request):
    posto = Posto.objects.all()
    context = {
       'posto_list': posto
    }
    return render(request, 'postos/list.html', context)