"""info419filme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
<<<<<<< HEAD
from core.views import genero, genero_cadastro, editar, remover

=======
from core.views import index, galeria, registro, perfil, filmes, genero, meus_dados
from django.contrib.auth import views as auth_views
>>>>>>> 9ba0568778b8e0bc3e72e537b0400bf48cf7413f
urlpatterns = [
	path('', index, name='index'),


    path('galeria/',galeria, name="galeria"),
    path('filmes/',filmes, name="filmes"),
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
<<<<<<< HEAD
    path('genero/',genero, name="genero"),
    path('genero_cadastro/',genero_cadastro, name="genero_cadastro"),
    path('editar/<int:id>/', editar, name='editar'),
    path('remover/<int:id>/', remover, name='remover'),
]
=======
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

>>>>>>> 9ba0568778b8e0bc3e72e537b0400bf48cf7413f
