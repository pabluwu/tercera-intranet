from django.forms import ModelForm, DateInput, TextInput
from intranet.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

class UsuarioProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('rut', 'telefono', 'fecha_ingreso', 'imagen', 'contacto')
        exclude = ['user']
        labels = {
            'contacto' : 'Contacto de Emergencia',
            'imagen' : 'Imagen de perfil'
        }
        widgets= {
            'fecha_ingreso' : DateInput(attrs={'readonly':'true'}),
            'rut' : DateInput(attrs={'readonly':'true'}),
        }

class UsuarioForm(ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name','username', 'email')
        widgets= {
            'username' : TextInput(attrs={'readonly':'true'}),
            'first_name' : TextInput(attrs={'readonly':'true'}),
            'last_name' : TextInput(attrs={'readonly':'true'})
        }
