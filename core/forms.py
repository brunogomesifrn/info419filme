class FilmesForm(ModelForm):
	class Meta():
		model = Filmes
		fields = ['titulo', 'duraçao', 'classificaçao', 'genero','fotos']