# coding=utf-8

from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View, TemplateView, CreateView
from django.contrib.auth import get_user_model
from django.contrib import messages

from .forms import ContactForm

User = get_user_model()

class IndexView(TemplateView):

    template_name = 'index.html'


index = IndexView.as_view()

class VacinaView(TemplateView):

    template_name = 'postos/vacinas/vacina.html'


vacina = VacinaView.as_view()

class RegistroVacinaView(TemplateView):

    template_name = 'postos/vacinas/registro_vacinas.html'


registro_vacina = RegistroVacinaView.as_view()

def contact(request):
    success = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_mail()
        success = True
    elif request.method == 'POST':
        messages.error(request, 'Formulário inválido')
    context = {
        'form': form,
        'success': success
    }
    return render(request, 'contact.html', context)



#
# class RegisterView(CreateView):
#
#     form_class = UserCreationForm
#     template_name = 'register.html'
#     model = User
#     success_url = reverse_lazy('index')
#
# register = RegisterView.as_view()
