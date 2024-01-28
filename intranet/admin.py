from django.contrib import admin
from .models import UserProfile, Citacion, Licencia, TipoDocumento, Documento, Cuota
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Citacion)
admin.site.register(Licencia)
admin.site.register(TipoDocumento)
admin.site.register(Documento)
admin.site.register(Cuota)