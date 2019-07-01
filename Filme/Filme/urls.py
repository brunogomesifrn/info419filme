from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from core.views import home, login, galeria, cadastro, perfil, filmes, genero, meus_dados, genero_cadastro, editar, remover, filmess, filme_cadastro

urlpatterns = [

    path('admin/', admin.site.urls),
    path('' ,home, name="home"),
    path('login/',login, name="login"),
    path('galeria/',galeria, name="galeria"),
    path('cadastro/',cadastro, name="cadastro"),
    path('perfil/',perfil, name="perfil"),
    path('filmes/',filmes, name="filmes"),
    path('genero/',genero, name="genero"),
    path('meus_dados/',meus_dados, name="meus_dados"),
    path('genero_cadastro/',genero_cadastro, name="genero_cadastro"),
    path('editar/<int:id>/', editar, name='editar'),
    path('remover/<int:id>/', remover, name='remover'),
    path('filmess/', filmess, name="filmess"),
    path('filme_cadastro/',filme_cadastro, name="filme_cadastro"),

    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
