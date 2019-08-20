from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.posto_list, name='posto_list'),
    #url(r'^detalhes_posto/(?P<slug>[\w_-]+)/$', views.posto),
    url(r'^detalhes_posto/(?P<slug>[-\w]+)/$', views.posto),
    url(r'^minhas_vacinas/', views.vacina, name='registro_vacina'),
    url(r'^minhas_vacinas/registro', views.registro_vacina, name='registro_vacina'),
]