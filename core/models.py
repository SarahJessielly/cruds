from django.db import models

class Curso(models.Model):
    titulo = models.CharField('Titulo', max_length=100)
    vagas = models.IntegerField('Vagas')

class Passagem(models.Model):
    origem = models.CharField('Origem', max_length=100)
    destino = models.CharField('Destino', max_length=100)
    valor = models.IntegerField('  Valor      ', max_length=100)

class Hospedagem(models.Model):
    foto = models.ImageField('Foto', upload_to='Hospedagem', null=True)
    nome = models.CharField('Nome', max_length=100)
    categoria = models.CharField('Categoria', max_length=100)
    localização = models.CharField('Localização', max_length=100)
    valor = models.IntegerField('Valor', max_length=100)
