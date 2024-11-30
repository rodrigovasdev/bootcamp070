
# importar la librería estándar de Django Forms
from django import forms
# Creación de un forms
class InputForm(forms.Form):
    Titulo = forms.CharField(max_length = 150)
    Autor = forms.CharField(max_length = 150)
    Valoracion = forms.IntegerField(min_value=0,max_value=10000)