
# importar la librería estándar de Django Forms
from django import forms
# import BoardsModel from models.py
from .models import BoardsModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Crear el BoardsForm
class BoardsForm(forms.ModelForm):
 # specify the name of model to use
    class Meta:
        model = BoardsModel
        fields = "__all__"

# Agregado para el registro de usuarios
class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    def save(self, commit=True):
        user = super(RegistroUsuarioForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
