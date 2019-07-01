from django.forms import ModelForm
from .models import filmes, Generos
from django import forms

class GenerosForm(ModelForm):
	class Meta():
		model = Generos
		fields = ['nome']

class FilmesForm(ModelForm):
	class Meta():
		model = filmes
		fields = ['titulo', 'duraçao', 'classificaçao', 'genero', 'fotos']
