
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from core.views import genero, genero_cadastro, editar, remover, filmess, filme_cadastro, index, galeria, registro, perfil, genero, meus_dados, foto1, foto2, foto3, foto4, foto5, foto6, foto7, foto8 
from django.contrib.auth import views as auth_views
urlpatterns = [
	path('', index, name='index'),


    path('galeria/',galeria, name="galeria"),
    path('genero/',genero, name="genero"),
	#perfil
	path('perfil/', perfil, name='perfil'),
	
	#registro de usuário
	path('registro/', registro, name='registro'),
	path('meus_dados/<int:id>/', meus_dados, name='meus_dados'),



	#autenticação
	path('login/', auth_views.LoginView.as_view(), name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('genero/',genero, name="genero"),
    path('genero_cadastro/',genero_cadastro, name="genero_cadastro"),
    path('editar/<int:id>/', editar, name='editar'),
    path('remover/<int:id>/', remover, name='remover'),
    path('filmess/', filmess, name="filmess"),
    path('filme_cadastro/',filme_cadastro, name="filme_cadastro"),


    #galeria
    path('foto1/', foto1, name="foto1"),
    path('foto2/', foto2, name="foto2"),
    path('foto3/', foto3, name="foto3"),
    path('foto4/', foto4, name="foto4"),
    path('foto5/', foto5, name="foto5"),
    path('foto6/', foto6, name="foto6"),
    path('foto7/', foto7, name="foto7"),
    path('foto8/', foto8, name="foto8"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


