
# importar la librería estándar de Django Forms
from django import forms
# import BoardsModel from models.py
from .models import BoardsModel
# Crear el BoardsForm
class BoardsForm(forms.ModelForm):
 # specify the name of model to use
    class Meta:
        model = BoardsModel
        fields = "__all__"
