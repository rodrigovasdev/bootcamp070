# Generated by Django 5.1.4 on 2025-01-09 22:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Biblioteca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('fecha_publicacion', models.DateField()),
                ('estado', models.CharField(choices=[('DISPONIBLE', 'Disponible'), ('PRESTADO', 'Prestado')])),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.autor')),
                ('biblioteca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.biblioteca')),
            ],
        ),
    ]
