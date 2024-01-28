from django.urls import path
from .views import citaciones_list, citaciones_post
from .views import post_licencia, licencia_list, licencia_revisar, licencia_citacion, licencia_list_historico, get_licencia
from .views import get_tipo_documento, all_tipo_documento, post_tipo_documento, delete_tipo_documento
from .views import post_documento, get_documento, list_documento, delete_documento
from .views import list_cuota

urlpatterns = [
    path("citaciones", citaciones_list, name="citaciones_list"),
    path("citaciones/crear", citaciones_post, name="citaciones_post"),

    path('licencia/<int:id>', post_licencia, name='post_licencia'),
    path('licencias/', licencia_list, name='licencia_list'),
    path('licencias/<int:id>', get_licencia, name='licencia_get'),
    path('licencias/historico', licencia_list_historico, name='licencia_list_historico'),
    path('licencias/revisar/', licencia_revisar, name='licencia_revisar'),
    path('licencias/revisar/<int:id_citacion>', licencia_citacion, name='licencia_citacion'),

    path('documentos/tipo/', all_tipo_documento, name='all_tipos_documentos'),
    path('documentos/tipo/<int:id>', get_tipo_documento, name='get_tipos_documentos'),
    path('documentos/tipo/delete/<int:id>', delete_tipo_documento, name='delete_tipo_documento'),
    path('documentos/tipo/crear', post_tipo_documento, name='post_tipos_documentos'),

    path('documentos/upload', post_documento, name='post_documento'),
    path('documentos/file/<str:file_name>', get_documento, name='get_documento'),
    path('documentos/', list_documento, name='list_documento'),
    path('documentos/delete/<int:id>', delete_documento, name='delete_documento'),
    
    path('cuotas/mis_cuotas', list_cuota, name='list_cuota'),
    
]