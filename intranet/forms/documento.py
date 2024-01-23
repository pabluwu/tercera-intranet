from django import forms 
from intranet.models import Documento
from django.core.exceptions import ValidationError

class DocumentoForm(forms.ModelForm):

    class Meta: 
        model = Documento
        fields = '__all__'
        exclude = ['nombre_original', 'ruta']
