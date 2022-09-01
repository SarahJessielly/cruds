"""Cursos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin 
from django .conf import settings
from django .conf.urls.static import static
from django.urls import path
from core.views import listar_cursos
from core.views import cadastrar_cursos, editar_curso, remover_curso, travels, listar_hospedagem, cadastrar_hospedagem
from core.views import listar_passagens, cadastrar_passagem, editar_passagem, remover_passagem, editar_hospedagem, remover_hospedagem

urlpatterns = [
    path('Cursos/', listar_cursos, name='listar_cursos'), 
    path('Cadastrar_Cursos/', cadastrar_cursos, name='cadastrar_cursos'),
    path('Editar_Cursos/<int:id>/', editar_curso, name='editar_curso'),
    path('Remover_Cursos/<int:id>/', remover_curso, name='remover_curso'),
    path('Travels/', travels, name='travels'),
    path('Hospedagens/', listar_hospedagem, name='listar_hospedagem'),
    path('Cadastrar_Hospedagens', cadastrar_hospedagem, name='cadastrar_hospedagem'),
    path('Editar_Hospedagens/<int:id>/', editar_hospedagem, name='editar_hospedagem'),
    path('Remover_Hospedagens/<int:id>/', remover_hospedagem, name='remover_hospedagem'),
    path('Passagens/', listar_passagens, name='listar_passagens'),
    path('Cadastrar_Passagens', cadastrar_passagem, name='cadastrar_passagem'),
    path('Editar_Passagens/<int:id>/', editar_passagem, name='editar_passagem'),
    path('Remover_Passagens/<int:id>/', remover_passagem, name='remover_passagem'),

    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
