from django import forms 
from intranet.models import Cuota

class CuotaForm(forms.ModelForm):

    class Meta: 
        model = Cuota
        fields = '__all__'
        widgets= {
            'fecha_ingreso' : forms.DateInput(attrs={'type':'date'})
        }
