from django import forms
from .models import Sala, Reserva

class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala  
        fields = '__all__' 

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva  
        fields = '__all__'
        widgets = {
            'hora_inicio': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local',  
            }),
            'hora_fin': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local',
            }),
        }