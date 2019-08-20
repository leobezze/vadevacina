from django.shortcuts import render
from .models import Posto, Vacina
from .forms import VacinaForm

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


def registro_vacina(request):
     if request.method == "POST":
         form = VacinaForm(request.POST)
         if form.is_valid():
             post = form.save(commit=False)
             post.author = request.user
             post.published_date = timezone.now()
             post.save()
             return redirect('vacina_detail', pk=post.pk)
     else:
         form = VacinaForm()
     return render(request, 'postos/Vacinas/registro_vacinas.html', {'form': form})