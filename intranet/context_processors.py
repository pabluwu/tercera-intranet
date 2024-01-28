from .models import TipoDocumento
from .models import UserProfile

def tipo_documento_base(request):
    tipos = TipoDocumento.objects.all()
    return { 'tipos_documento' : tipos }

def user_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    return user_profile
    

