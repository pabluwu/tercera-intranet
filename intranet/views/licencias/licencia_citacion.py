from django.http import HttpResponse
from django.shortcuts import render
from intranet.models import Licencia, Citacion
from django.http import Http404
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required

@login_required
def licencia_citacion(request, id_citacion):
    current_date = datetime.now().date()
    current_datetime = datetime.now()

    
    citaciones = Citacion.objects.filter(fecha__gt=current_date)
    

    return render(request, './licencias/licencia_citacion.html', {"citaciones": citaciones, "current_datetime": current_datetime})
    
    
    