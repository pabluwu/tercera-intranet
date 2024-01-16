from django.http import HttpResponse
from django.shortcuts import render
from intranet.models import Licencia, Citacion
from django.http import Http404
from datetime import datetime, timedelta
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.admin import User

@login_required
def licencia_citacion(request, id_citacion):
    
    citacion = get_object_or_404(Citacion, id=id_citacion)

    current_datetime = datetime.now()

    licencias = Licencia.objects.filter(citacion_id=citacion.id).select_related("autor")

    for l in licencias:
        print(l.autor)

    context = {
        'current_datetime' : current_datetime,
        'citacion' : citacion,
        'licencias' : licencias,
    }
    

    return render(request, './licencias/licencia_citacion.html', context)
    
    
    