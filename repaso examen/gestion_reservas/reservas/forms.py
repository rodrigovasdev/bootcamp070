from django import forms
from .models import Sala, Reserva

class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala  
        fields = '__all__' 
