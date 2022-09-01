# Generated by Django 4.1 on 2022-09-01 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo')),
                ('vagas', models.IntegerField(verbose_name='Vagas')),
                ('foto', models.ImageField(null=True, upload_to='curos', verbose_name='Foto')),
            ],
        ),
        migrations.CreateModel(
            name='Hospedagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.CharField(max_length=100, verbose_name='Foto')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('categoria', models.CharField(max_length=100, verbose_name='Categoria')),
                ('localização', models.CharField(max_length=100, verbose_name='Localização')),
                ('valor', models.IntegerField(max_length=100, verbose_name='Valor')),
            ],
        ),
        migrations.CreateModel(
            name='Passagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origem', models.CharField(max_length=100, verbose_name='Origem')),
                ('destino', models.CharField(max_length=100, verbose_name='Destino')),
                ('valor', models.IntegerField(max_length=100, verbose_name='Valor')),
            ],
        ),
    ]