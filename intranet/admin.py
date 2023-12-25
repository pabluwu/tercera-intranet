from django.contrib import admin
from .models import UserProfile, Citacion, Licencia
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Citacion)
admin.site.register(Licencia)