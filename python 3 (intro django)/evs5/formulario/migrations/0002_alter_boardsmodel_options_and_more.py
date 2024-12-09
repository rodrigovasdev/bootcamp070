# Generated by Django 4.2.16 on 2024-12-07 00:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='boardsmodel',
            options={'permissions': (('es_miembro_1', 'Es miembro con prioridad 1'),)},
        ),
        migrations.RemoveField(
            model_name='boardsmodel',
            name='modificado',
        ),
        migrations.AddField(
            model_name='boardsmodel',
            name='valoracion',
            field=models.IntegerField(default=datetime.datetime(2024, 12, 7, 0, 10, 33, 40492, tzinfo=datetime.timezone.utc), help_text='Valor entre 0 y 10000'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='boardsmodel',
            name='descripcion',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='boardsmodel',
            name='titulo',
            field=models.CharField(max_length=5),
        ),
    ]