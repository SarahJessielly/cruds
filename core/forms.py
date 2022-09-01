from django.forms import ModelForm 
from .models import Curso, Passagem, Hospedagem

class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = ['titulo', 'vagas']

class PassagemForm(ModelForm):
    class Meta:
        model = Passagem
        fields = ['origem', 'destino', 'valor']

class HospedagemForm(ModelForm):
    class Meta:
        model = Hospedagem
        fields = ['foto', 'nome', 'categoria', 'localização', 'valor']