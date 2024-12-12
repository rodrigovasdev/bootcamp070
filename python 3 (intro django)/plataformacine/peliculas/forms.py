# importar la librería estándar de Django Forms
from django import forms
# import BoardsModel from models.py
from .models import PeliculaModel
# Crear el BoardsForm
class PeliculaForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = PeliculaModel
        fields = '__all__'
