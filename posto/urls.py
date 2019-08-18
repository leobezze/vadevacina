from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.posto_list),
    url(r'^listagem_de_postos/(?P<slug>[\w_-]+)/$', views.posto),
    #url(r'^posts/(?P<slug>[-\w]+)/$', views.post, name='post'),
    url(r'^minhas_vacinas/', views.vacina),
]