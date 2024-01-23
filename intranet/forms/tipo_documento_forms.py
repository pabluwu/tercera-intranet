from django import forms 
from intranet.models import TipoDocumento

class TipoDocumentoForm(forms.ModelForm):

    class Meta: 
        model = TipoDocumento
        fields = '__all__'
        exclude = ['slug']