import os
from django.http import FileResponse
from intranet.models import Documento, TipoDocumento
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required


from intranet.forms import DocumentoForm

@login_required
def get_documento(request, file_name):
    # documento = get_object_or_404(Documento, pk=id)
    documento = Documento.objects.get(nombre_original=file_name)

    print(documento.archivo.name)
    # filepath = os.path.join('uploads/', str(documento.archivo.name))
    filepath = documento.archivo.path
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')

@login_required
def list_documento(request):
    try:
        tipo_documento = TipoDocumento.objects.get(slug=request.GET.get('type'))
        documentos = Documento.objects.filter(tipo_documento=tipo_documento)
        context = {'documentos' : documentos, 'tipo' : tipo_documento}
    except:
        documentos = Documento.objects.all()
        context = {'documentos' : documentos}


    if not documentos:
        context['empty'] = True 
    
    print(documentos)
    return render(request, './documento/list.html', context)
    print(documento.archivo)
    filepath = os.path.join('', str(documento.archivo))
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')