from django import forms
from .models import LibroModel

class LibroForm(forms.ModelForm):
 # specify the name of model to use
    class Meta:
        model = LibroModel
        fields = "__all__"
