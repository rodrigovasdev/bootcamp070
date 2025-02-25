# Generated by Django 4.2.18 on 2025-01-14 22:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('capacidad', models.IntegerField()),
                ('ubicacion', models.CharField(max_length=50)),
                ('equipamiento', models.TextField()),
                ('disponibilidad', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cliente', models.CharField(max_length=50)),
                ('hora_inicio', models.DateTimeField()),
                ('hora_fin', models.DateTimeField()),
                ('estado', models.CharField(choices=[('Confirmada', 'confirmada'), ('Pendiente', 'pendiente'), ('Cancelada', 'cancelada')], max_length=50)),
                ('sala', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservas.sala')),
            ],
        ),
    ]
