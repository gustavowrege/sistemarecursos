# -*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from .forms import addRecursoForm, loginCandidatoForm, addEtapaRecursoForm, addCandidatosForm
from django.utils import timezone
from .models import EtapaRecurso, Recurso, Candidato
from django.contrib.auth import authenticate, login
import datetime
from io import TextIOWrapper
import csv

def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")

def listar_etapas(request):
	try:
		etapasRecurso = EtapaRecurso.objects.all()

	except EtapaRecurso.DoesNotExist:
		raise Http404("Este edital nao existe")


	return render(request, 'sistemarecursos/listar_etapas.html', {'etapas' : etapasRecurso})


def etaparecurso(request, etapa_id):

	etaparecurso = get_object_or_404(EtapaRecurso, id=etapa_id)
	agora = timezone.now()
	erro = None

	if request.method == "POST":
		form = loginCandidatoForm(request.POST)

		if form.is_valid():
			#testar se candidato esta inscrito
			inscricao = form.cleaned_data['inscricao']
			rg = form.cleaned_data['rg']

			candidato = Candidato.objects.filter(inscricao=inscricao, rg=rg, etapaRecurso=etaparecurso)
			if Candidato.objects.filter(inscricao=inscricao, rg=rg, etapaRecurso=etaparecurso):
				request.session['candidato'] = inscricao

				return redirect('addrecurso', etapa_id=etapa_id)

			else:
				return render(request, 'sistemarecursos/detalhe_etapa.html', {'etapa' : etaparecurso, 'agora': agora, 'form' : form, 'erro': 'erro', 'msg':"Candidato não encontrado"})

	else:
		form = loginCandidatoForm()

	return render(request, 'sistemarecursos/detalhe_etapa.html', {'etapa' : etaparecurso, 'agora': agora, 'form' : form})

def addrecurso(request, etapa_id):
	etaparecurso = get_object_or_404(EtapaRecurso, id=etapa_id)
	candidato = Candidato.objects.get(inscricao=request.session['candidato'])
	if request.method == "POST":
		form = addRecursoForm(request.POST)

		if form.is_valid():
			recurso = form.save(commit=False)
			recurso.timestamp = timezone.now()
			recurso.candidato = candidato

			if request.POST.get('solicitacao', None) == "anular":
				recurso.solicitacao = "Anular questão"
			elif request.POST.get('solicitacao', None) == "alterar":
				de = request.POST.get('de', None).upper()
				para = request.POST.get('para', None).upper()
				recurso.solicitacao = "Alterar gabarito de %s para %s" % (de,para)
			#recurso.solicitacao = solicitacao
			#recurso.etapaRecurso.id = etapa_id EtapaRecurso.objects.filter(id=etapa_id)
			recurso.save()
			request.session['recurso_id'] = recurso.id
			return redirect('confirmarecurso', etapa_id=etapa_id)
			#return render(request, 'sistemarecursos/confirmarecurso.html', {'recurso' : recurso})

	else:
		form = addRecursoForm()

	return render(request, 'sistemarecursos/addrecurso.html', {'etapa' : etaparecurso, 'form': form, 'candidato': candidato})

def editarecurso(request, etapa_id):
	etaparecurso = get_object_or_404(EtapaRecurso, id=etapa_id)
	candidato = Candidato.objects.get(inscricao=request.session['candidato'])
	recurso = Recurso.objects.get(id=request.session['recurso_id'])

	if "Anular" in recurso.solicitacao:
		solicitacao = "anular"
		de = ""
		para = ""
	else:
		solicitacao = "alterar"
		de = recurso.solicitacao.split(" ")[3]
		para = recurso.solicitacao.split(" ")[5]

	if request.method == "POST":
		form = addRecursoForm(request.POST, instance=recurso)

		if form.is_valid():
			recurso = form.save(commit=False)
			recurso.timestamp = timezone.now()
			candidato = Candidato.objects.get(inscricao=request.session['candidato'])
			recurso.candidato = candidato

			if request.POST.get('solicitacao', None) == "anular":
				recurso.solicitacao = "Anular questão"
			elif request.POST.get('solicitacao', None) == "alterar":
				de = request.POST.get('de', None).upper()
				para = request.POST.get('para', None).upper()
				recurso.solicitacao = "Alterar gabarito de %s para %s" % (de, para)

			recurso.save()
			request.session['recurso_id'] = recurso.id
			return redirect('confirmarecurso', etapa_id=etapa_id)

	else:
		form = addRecursoForm(instance=recurso)

	return render(request, 'sistemarecursos/addrecurso.html', {'etapa' : etaparecurso, 'form': form, 'candidato': candidato, 'solicitacao': solicitacao, 'de': de, 'para':para})

def confirmarecurso(request, etapa_id):
	etaparecurso = get_object_or_404(EtapaRecurso, id=etapa_id)
	recurso = Recurso.objects.get(id=request.session['recurso_id'])

	if request.method == "POST":
		if request.POST.get("confirmar"):
			return render(request, 'sistemarecursos/enviarecurso.html', {'etapa' : etaparecurso, 'recurso' : recurso, 'msg': "Recurso enviado com sucesso!\n Verifique a confirmação no seu email."})

		elif request.POST.get("editar"):
			return redirect('editarecurso', etapa_id=etapa_id)

		elif request.POST.get("novo"):
			return redirect('addrecurso', etapa_id=etapa_id)

		elif request.POST.get("sair"):
			return redirect('etaparecurso', etapa_id=etapa_id)

	return render(request, 'sistemarecursos/confirmarecurso.html', {'etapa' : etaparecurso, 'recurso' : recurso})


def listar_recursos(request, etapa_id):
	try:
		recursos = Recurso.objects.filter(etapaRecurso=etapa_id)

	except Recurso.DoesNotExist:
		raise Http404("Este edital nao existe")

	return render(request, 'sistemarecursos/listar_recursos.html', {'recursos' : recursos})

def admin(request):

	try:
		etapasRecurso = EtapaRecurso.objects.all()

	except EtapaRecurso.DoesNotExist:
		raise Http404("Este edital nao existe")


	return render(request, 'sistemarecursos/admin.html', {'etapas' : etapasRecurso})

def addEtapaRecurso(request):

	if request.method == "POST":
		form = addEtapaRecursoForm(request.POST)

		if form.is_valid():
			etapaRecurso = form.save(commit=False)
			etapaRecurso.save()
			return redirect('addCandidatos', etapaRecurso.id)

	else:
		form = addEtapaRecursoForm()

	return render(request, 'sistemarecursos/addEtapaRecurso.html', {'form': form})

def addCandidatos(request, etapa_id):
	etapaRecurso = get_object_or_404(EtapaRecurso, id=etapa_id)
	string = ""
	if request.method == 'POST':
		form = addCandidatosForm(request.POST, request.FILES)

		if form.is_valid:

			for linha in request.FILES['file']:
				campos = linha.split(';')
				nome = campos[1]
				inscricao = campos[0]
				rg = campos[3]
				cargo_area = campos[2]
				email = campos[4]

				candidato = Candidato.objects.create(etapaRecurso=etapaRecurso, nome=nome, inscricao=inscricao, rg=rg, cargo_area=cargo_area, email=email)

			return redirect('admin')

	else:
		form = addCandidatosForm()

	return render(request, 'sistemarecursos/addCandidatos.html', {'form': form, 'etapa': etapaRecurso, 'str': string})
