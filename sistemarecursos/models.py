# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

class EtapaRecurso(models.Model):
	edital = models.CharField(max_length=200)
	tipoProva = models.CharField(max_length=200)
	dataAbertura = models.DateTimeField('Data Abertura')
	dataFechamento = models.DateTimeField('Data Fechamento')

	def __str__(self):
		return self.edital

	def ativo(self):
		agora = timezone.now()
		if (agora >= self.dataAbertura) and (agora <= self.dataFechamento):
			return True
		else:
			return False

class Candidato(models.Model):
	etapaRecurso = models.ForeignKey(EtapaRecurso, on_delete=models.CASCADE)
	nome = models.CharField(max_length=200)
	inscricao = models.CharField(max_length=10)
	rg = models.CharField(max_length=14)
	cargo_area = models.CharField(max_length=200)
	email = models.EmailField()

	def __unicode__(self):
		return self.nome

	def __str__(self):
		return self.nome

class Recurso(models.Model):
	candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
	questao = models.CharField(max_length=2)
	solicitacao = models.CharField(max_length=40)
	textoRecurso = RichTextField(max_length=5000)
	timestamp = models.DateTimeField('Data de Subsmissao')

	def __str__(self):
		return self.questao
