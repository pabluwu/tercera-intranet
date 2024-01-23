from django.shortcuts import render, redirect
from intranet.models import TipoDocumento
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages

from intranet.forms import TipoDocumentoForm


@login_required
@permission_required('intranet.view_tipodocumento')
def all_tipo_documento(request):

    tipo_documento = TipoDocumento.objects.all()

    context = { 'tipo_documento' : tipo_documento }

    return render(request, './tipo_documento/list.html', context)

@login_required
@permission_required('intranet.view_tipodocumento')
def get_tipo_documento(request, id):

    tipo_documento = get_object_or_404(TipoDocumento, id=id)

    context = { 'form' : TipoDocumentoForm(instance = tipo_documento) }
    
    if request.method == 'POST':
        form = TipoDocumentoForm(request.POST, instance=tipo_documento)

        if form.is_valid():
            form.save()
            messages.success(request, "Tipo documento actualizado correctamente")
            context['form'] = form
            return redirect(to='all_tipos_documentos')
        

    return render(request, './tipo_documento/get.html', context)