from django.shortcuts import render

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

def filmess(request):
	
	return render(request, 'filmess.html', var)
	
def filme_cadastro(request):
	

	return render(request, 'filme_cadastro.html', var)
	

