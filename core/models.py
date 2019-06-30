from django.db import models

class genero(models.Model):
	nome = models.CharField('Nome', max_length=100)

class filmes(models.Model):
	titulo = models.CharField('Titulo', max_length=100)
	duraçao = models.CharField('Duraçao', max_length=100)
	classificaçao = models.CharField('classificação', max_length=100)
	genero = models.ManyToManyField(genero)
	fotos = models.ImageField('Fotos', upload_to='filmes', null=True)
# Create your models here.
