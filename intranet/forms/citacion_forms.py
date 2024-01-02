from django import forms 
from intranet.models import Citacion
from datetime import datetime
from django.contrib.admin.widgets import AdminTimeWidget
from django.core.exceptions import ValidationError

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

    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha', False)
        if fecha < datetime.now():
            raise ValidationError("Fecha no puede ser anterior a hoy.")
        else:
            return fecha
