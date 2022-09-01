from django.shortcuts import render, redirect
from .models import Curso, Hospedagem, Passagem
from .forms import CursoForm, PassagemForm, HospedagemForm


def travels(request):
    return render(request, 'templates/pagina_principal.html')



def listar_cursos(request):
    variavel_curso = Curso.objects.all()
    contexto = {
        'todos_cursos': variavel_curso
    }
    return render(request, 'templates/cursos.html', contexto)



def cadastrar_cursos(request):
    formulario = CursoForm(request.POST or None)

    if formulario.is_valid():
        formulario.save()
        return redirect('listar_cursos')

    contexto = {
        'form_curso': formulario
    } 
    return render(request, 'templates/cadastro_cursos.html', contexto) 




def editar_curso(request, id):
    curso = Curso.objects.get(pk=id)
    
    form= CursoForm(request.POST or None, instance=curso)
    
    if form.is_valid():
        form.save()
        return redirect('listar_cursos')

    contexto = {
        'form_curso': form
    }

    return render(request, 'templates/cadastro_cursos.html', contexto)



def remover_curso(request, id):
    curso = Curso.objects.get(pk=id)
    curso.delete()
    return redirect('listar_cursos')



def listar_hospedagem(request):
    variavel_hospedagem = Hospedagem.objects.all()
    contexto = {
        'todas_hospedagens': variavel_hospedagem
    }
    return render(request, 'templates/hospedagem.html', contexto)



def cadastrar_hospedagem(request):
    formulario = HospedagemForm(request.POST or None, request.FILES or None)

    if formulario.is_valid():
        formulario.save()
        return redirect('listar_hospedagem')

    contexto = {
        'form_hospedagem': formulario
    } 
    return render(request, 'templates/cadastro_hospedagens.html', contexto)

def editar_hospedagem(request, id):
    hosp = Hospedagem.objects.get(pk=id)
    
    formulario= HospedagemForm(request.POST or None, instance=hosp)
    
    if formulario.is_valid():
        formulario.save()
        return redirect('listar_hospedagem')

    contexto = {
        'form_hospedagem': formulario
    }

    return render(request, 'templates/cadastro_hospedagens.html', contexto)


def remover_hospedagem(request, id):
    formulario = Hospedagem.objects.get(pk=id)
    formulario.delete()
    return redirect('listar_hospedagem')


def listar_passagens(request):
    variavel_passagem = Passagem.objects.all()
    contexto = {
        'todas_passagens': variavel_passagem
    }
    return render(request, 'templates/passagens.html', contexto)



def cadastrar_passagem(request):
    formulario = PassagemForm(request.POST or None)

    if formulario.is_valid():
        formulario.save()
        return redirect('listar_passagens')

    contexto = {
        'form_passagem': formulario
    } 
    return render(request, 'templates/cadastro_passagens.html', contexto)

def editar_passagem(request, id):
    passagem = Passagem.objects.get(pk=id)
    
    formulario= PassagemForm(request.POST or None, instance=passagem)
    
    if formulario.is_valid():
        formulario.save()
        return redirect('listar_passagens')

    contexto = {
        'form_passagem': formulario
    }

    return render(request, 'templates/cadastro_passagens.html', contexto)


def remover_passagem(request, id):
    formulario = Passagem.objects.get(pk=id)
    formulario.delete()
    return redirect('listar_passagens')