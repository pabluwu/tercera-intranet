from django.shortcuts import render
from intranet.models import TipoDocumento
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.shortcuts import redirect
from slugify import slugify

from intranet.forms import TipoDocumentoForm

@login_required
@permission_required('intranet.add_tipodocumento')
def post_tipo_documento(request):

    context = { 'form' : TipoDocumentoForm() }
    
    if request.method == 'POST':
        form = TipoDocumentoForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.slug = slugify(obj.tipo)
            obj.save()
            messages.success(request, "Tipo documento añadido correctamente")
            context['form'] = form
            return redirect(to='all_tipos_documentos')
        

    return render(request, './tipo_documento/post.html', context)

@login_required
@permission_required('intranet.delete_tipodocumento')
def delete_tipo_documento(request, id):
    
    tipo_documento = get_object_or_404(TipoDocumento, pk=id)
    
    tipo_documento.delete()
    
    return redirect(to='all_tipos_documentos')