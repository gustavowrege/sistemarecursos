# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from . import views

urlpatterns = [
	
	url(r'^$', views.index, name='index'),
	url(r'^admin/$', views.admin, name='admin'),
	url(r'^admin/addEtapaRecurso/$', views.addEtapaRecurso, name='addEtapaRecurso'),
	url(r'^admin/(?P<etapa_id>[0-9]+)/addCandidatos/$', views.addCandidatos, name='addCandidatos'),
	url(r'^listar_etapas/$', views.listar_etapas, name='listar_etapas'),
	url(r'^(?P<etapa_id>[0-9]+)/$', views.etaparecurso, name='etaparecurso'),
	url(r'^(?P<etapa_id>[0-9]+)/addrecurso/$', views.addrecurso, name='addrecurso'),
	url(r'^(?P<etapa_id>[0-9]+)/editarecurso/$', views.editarecurso, name='editarecurso'),
	url(r'^(?P<etapa_id>[0-9]+)/confirmarecurso/$', views.confirmarecurso, name='confirmarecurso'),
	url(r'^(?P<etapa_id>[0-9]+)/listar_recursos/$', views.listar_recursos, name='listar_recursos')
]
