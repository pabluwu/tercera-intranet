from django.http import HttpResponse
from django.shortcuts import render
from intranet.models import Citacion
from django.http import Http404
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect, reverse
from django.contrib import messages

from intranet.forms import CitacionForm

@login_required
@permission_required('intranet.add_citacion')
def citaciones_post(request):
    current_datetime = datetime.now()
    context = {"form": CitacionForm(), "current_datetime": current_datetime}

    if request.method == 'POST':
        formulario = CitacionForm(data=request.POST)
        if formulario.is_valid():
            new_citacion = formulario.save(commit=False)
            
            time_change = timedelta(hours=formulario.cleaned_data['hora'].hour, minutes=formulario.cleaned_data['hora'].minute)
            new_citacion.fecha = new_citacion.fecha+time_change
            new_citacion.save()
            messages.success(request, "Citación creada correctamente")
        else:
            context['form'] = formulario

    return render(request, './citaciones/post.html', context)
    
    
    