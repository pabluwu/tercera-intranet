from .citaciones.citaciones_list import citaciones_list
from .citaciones.citaciones_post import citaciones_post
from .citaciones.citaciones_anteriores import citaciones_anteriores
from .licencias.licencia_post import post_licencia
from .licencias.licencia_list import licencia_list
from .licencias.licencia_revisar import licencia_revisar
from .licencias.licencia_citacion import licencia_citacion
from .licencias.licencia_list_historico import licencia_list_historico
from .licencias.licencia_get import get_licencia
from .tipo_documento.get import get_tipo_documento
from .tipo_documento.get import all_tipo_documento
from .tipo_documento.post import post_tipo_documento, delete_tipo_documento
from .documento.post import post_documento, delete_documento
from .documento.get import get_documento, list_documento
from .cuota.get import list_cuota
from .cuota.post import post_cuota
from .usuario.editar_perfil import editar_perfil