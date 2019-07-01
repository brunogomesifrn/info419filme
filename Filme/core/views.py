from django.shortcuts import render, redirect
from .models import Generos, filmes
from .forms import FilmesForm, GenerosForm

def home(request):
	return render(request, 'index.html')

def login(request):
	return render(request, 'login.html')

def galeria(request):
	return render(request, 'galeria.html')

def cadastro(request):
	return render(request, 'cadastro.html')

def perfil(request):
	return render(request, 'perfil.html')

def filmes(request):
	return render(request, 'filmes.html')

def genero(request):
	gen = Generos.objects.all()
	var = {
	'genero': gen
	}
	return render(request, 'genero.html', var)

def meus_dados(request):
	return render(request, 'meus_dados.html')

def genero_cadastro(request):
	gen = GenerosForm(request.POST or None)
	if gen.is_valid():
		gen.save ()
		return redirect('genero')

	gen = GenerosForm()
	var = {
	'gen': gen
	}

	return render(request, 'genero_cadastro.html', var)
	
def editar(request, id):
	gen = Generos.objects.get(pk=id)
	gen = GenerosForm(request.POST or None, request.FILES or None, instance=gen)
	if gen.is_valid():
		gen.save()
		return redirect('genero')

	contexto = {
		'gen': gen
	}

	return render(request, 'genero_cadastro.html', contexto)


def remover(request, id):
	gen = Generos.objects.get(pk=id)
	gen .delete()

	return redirect('genero')


def filmess(request):
	fil = fil.objects.all()
	var = {
	'filmes': fil
	}
	return render(request, 'filmess.html', var)
	
def filme_cadastro(request):
	fil = FilmesForm(request.POST or None)
	if fil.is_valid():
		fil.save ()
		return redirect('filmes')

	fil = FilmesForm()
	var = {
	'fil': fil
	}

	return render(request, 'filme_cadastro.html', var)
	

	
	
	

