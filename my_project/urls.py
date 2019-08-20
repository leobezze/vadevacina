"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.views.static import serve as serve_static
from django.contrib.auth.views import login, logout

from core import views


urlpatterns = [
    path('', views.index, name='index'),
    path('minhas_vacinas/', views.vacina, name='vacina'),
    path('minhas_vacinas/registro', views.registro_vacina, name='registro_vacina'),
    path('contato/', views.contact, name='contact'),
    path('entrar/', login, {'template_name':'login.html'}, name='login'),
    path('sair/', logout, {'next_page':'index'}, name='logout'),
    path('conta/', include('accounts.urls', namespace='accounts')),
    path('postos/', include(('posto.urls', 'posto'), namespace='posto')),
    path('admin/', admin.site.urls),
]
