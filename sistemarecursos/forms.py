# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from .models import Recurso, Candidato, EtapaRecurso
from ckeditor.widgets import CKEditorWidget
from django.forms.widgets import RadioSelect

RADIO_CHOICES = [['1','Anular'],['2','Alterar gabarito']]

class addRecursoForm(forms.ModelForm):
	class Meta:
		model = Recurso
		fields = ('questao', 'textoRecurso')
		widgets = {'questao': forms.TextInput(attrs={'class': 'form-control', 'style': "width:"})}

	def __init__(self, *args, **kwargs):
		super(addRecursoForm, self).__init__(*args, **kwargs)
		# add custom error messages
		self.fields['textoRecurso'].error_messages = {'required': 'Please let us know what to call you!'}

class loginCandidatoForm(forms.Form):
	inscricao = forms.CharField(max_length=6, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Informe sua inscrição"}))
	rg = forms.CharField(max_length=11, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Informe seu RG"}))


class addEtapaRecursoForm(forms.ModelForm):

	class Meta:
		model = EtapaRecurso
		fields = ('edital', 'tipoProva', 'dataAbertura', 'dataFechamento')
		widgets = {'dataFechamento': forms.DateTimeInput(attrs={'class': 'datetime-input'}), 'dataAbertura': forms.DateTimeInput(attrs={'class': 'datetime-input'})}

class addCandidatosForm(forms.Form):
	file = forms.FileField()
