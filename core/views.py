from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Generos, filmes
from .forms import FilmesForm, GenerosForm

<<<<<<< HEAD
def foto1(request):
	return render(request, 'foto1.html')

def foto2(request):
	return render(request, 'foto2.html')

def foto3(request):
	return render(request, 'foto3.html')

def foto4(request):
	return render(request, 'foto4.html')

def foto5(request):
	return render(request, 'foto5.html')

def foto6(request):
	return render(request, 'foto6.html')

def foto7(request):
	return render(request, 'foto7.html')

def foto8(request):
	return render(request, 'foto8.html')
=======


def index(request):
	return render(request, 'index.html')

	
def registro(request):
	form = UserCreationForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('login')
	contexto = {
		'form':form
	}
	return render(request, 'registro.html', contexto)

@login_required
def perfil(request):
	return render(request, 'perfil.html')


@login_required
def meus_dados(request, id):
	user = User.objects.get(pk=id)
	form = UserCreationForm(request.POST or None, instance=user)
	if form.is_valid():
		form.save()
		return redirect('perfil')
	contexto = {
		'form': form
	}
	return render(request, 'registro.html', contexto)

def genero(request):

	gen = Generos.objects.all()
	var = {
	'genero': gen
	}
	return render(request, 'genero.html', var)

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

<<<<<<< HEAD
def filmess(request):
	
	return render(request, 'filmess.html', var)
	
def filme_cadastro(request):
	

	return render(request, 'filme_cadastro.html', var)
	

=======
>>>>>>> 77b1d1743a1a9a490ba08c7816fc78ed20dec915
>>>>>>> e0dacd05788db9b060534583efba035e57ededde
