from django.http import HttpResponse
from django.shortcuts import render
from intranet.models import Licencia, Citacion
from django.http import Http404
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required

@login_required
def licencia_list(request):
    current_date = datetime.now().date()
    current_datetime = datetime.now()

    licencias = Licencia.objects.filter(autor_id=request.user.id)
    obj = []
    for l in licencias:
        print(l.id)
        c = Citacion.objects.get(id=l.citacion_id)
        obj.append({'licencia':l,'citacion':c})

    return render(request, './licencias/list.html', {"licencias": obj, "current_datetime": current_datetime})
    
    
    