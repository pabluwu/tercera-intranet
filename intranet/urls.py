from django.urls import path
from .views import citaciones_list, citaciones_post
from .views import post_licencia, licencia_list, licencia_revisar, licencia_citacion, licencia_list_historico, get_licencia

urlpatterns = [
    path("citaciones", citaciones_list, name="citaciones_list"),
    path("citaciones/crear", citaciones_post, name="citaciones_post"),

    path('licencia/<int:id>', post_licencia, name='post_licencia'),
    path('licencias/', licencia_list, name='licencia_list'),
    path('licencias/<int:id>', get_licencia, name='licencia_get'),
    path('licencias/historico', licencia_list_historico, name='licencia_list_historico'),
    path('licencias/revisar/', licencia_revisar, name='licencia_revisar'),
    path('licencias/revisar/<int:id_citacion>', licencia_citacion, name='licencia_citacion'),
    
]