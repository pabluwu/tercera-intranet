from .models import TipoDocumento

def tipo_documento_base(request):
    tipos = TipoDocumento.objects.all()
    return { 'tipos_documento' : tipos }

