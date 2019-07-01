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
	genCads = GenerosForm(request.POST or None)
	if genCads.is_valid():
		genCads.save ()
		return redirect('genero')

	genCads = GenerosForm()
	var = {
	'gen': genCads
	}

	return render(request, 'genero_cadastro.html', var)
	
def editar(request, id):
	gen = Generos.objects.get(pk=id)
	form = GenerosForm(request.POST or None, request.FILES or None, instance=gen)
	if form.is_valid():
		form.save()
		return redirect('genero')

	contexto = {
		'form': form
	}

	return render(request, 'genero_cadastro.html', contexto)


def remover(request, id):
	gen = Generos.objects.get(pk=id)
	gen .delete()

	return redirect('genero')

def filmess(request):
	
	return render(request,'filmess.html')
	
	

def filme_cadastro(request):
	
	return render(request, 'filme_cadastro.html')

	
	
	

