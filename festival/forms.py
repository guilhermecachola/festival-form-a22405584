from django import forms
from .models import Concerto, Palco

class ConcertoForm(forms.ModelForm):
    class Meta:
        model = Concerto
        fields = "__all__" 
        
        widgets = {
            'hora': forms.TimeInput(attrs={'type': 'time'}),
        }

class PalcoForm(forms.ModelForm):
    class Meta:
        model = Palco
        fields = ["nome", "capacidade", "imagem"]