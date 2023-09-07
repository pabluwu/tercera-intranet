from django import forms 
from intranet.models import Licencia

class LicenciaForm(forms.ModelForm):

    class Meta: 
        model = Licencia
        fields = ['motivo']