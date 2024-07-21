from django.http import HttpResponse
from django.shortcuts import render
from intranet.models import UserProfile
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from intranet.forms import UsuarioForm, UsuarioProfileForm

@login_required
def editar_perfil(request):
    
    usuario = request.user
    
    usuario_profile_form = UsuarioProfileForm(instance=usuario.bombero)
    usuario_form = UsuarioForm(instance=usuario)
    
    if request.method == 'POST':
        usuario_form = UsuarioForm(request.POST, instance=usuario)
        usuario_profile_form = UsuarioProfileForm(request.POST, request.FILES, instance=usuario.bombero)
        
        if usuario_form.is_valid():
            usuario_form.save()
            
        if usuario_profile_form.is_valid():
            usuario_profile_form.save()
            
        messages.success(request, "Cambios aplicados correctamente")

    return render(request, './perfil/editar.html', { 'form' : usuario_form, 'form_profile' : usuario_profile_form} )
    
    
    