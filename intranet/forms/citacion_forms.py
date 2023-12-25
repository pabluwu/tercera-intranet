from django import forms 
from intranet.models import Citacion
from django.contrib.admin.widgets import AdminTimeWidget

class CitacionForm(forms.ModelForm):
    hora = forms.TimeField(label='Hora Citación', required=True, widget=AdminTimeWidget(attrs={'type':'text'}))
    class Meta: 
        model = Citacion
        fields = (
            'nombre',
            'descripcion',
            'fecha',
            'hora',
            'lugar',
            'tenida',
            'autor'
        )
        widgets= {
            'fecha' : forms.DateInput(attrs={'type':'date'})
        }