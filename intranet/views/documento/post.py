from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib import messages
from intranet.models import Documento

from intranet.forms import DocumentoForm

@login_required
@permission_required('intranet.add_documento')
def post_documento(request):

    context = { 'form' : DocumentoForm() }
    
    if request.method == 'POST':
        form = DocumentoForm(request.POST,  request.FILES)

        if form.is_valid():
            obj = form.save(commit=False)
            txt = request.FILES['archivo'].name
            obj.nombre_original = str(txt)
            print(obj.archivo)
            obj.save()
            messages.success(request, "Documento subido correctamente")
            context['form'] = form
        else:
            context['form'] = form
        

    return render(request, './documento/post.html', context)

@login_required
@permission_required('intranet.delete_documento')
def delete_documento(request, id):
    documento = get_object_or_404(Documento, pk=id)
    documento.archivo.delete()
    documento.delete()
    return redirect(to='list_documento')
        