from django.http import HttpResponse
from django.shortcuts import render
from intranet.models import Citacion, Licencia
from django.http import Http404
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required

@login_required
def citaciones_anteriores(request):
    current_date = datetime.now().date()
    current_datetime = datetime.now()
    
    year = request.GET.get('year')
    
    if year:
        try:
            if year == 'any':
                citaciones = Citacion.objects.filter(fecha__lte=current_date).order_by('fecha')
            else:
                citaciones = Citacion.objects.filter(fecha__lte=current_date, fecha__year=year).order_by('fecha')
            
            obj = []
            for c in citaciones:
                licencias = Licencia.objects.filter(citacion=c.id).count()
                print(f'Id citacion {c.id}, cantidad licencias {licencias}')
                obj.append({'citacion':c,'cantidad_licencias':licencias})
                           
        except Citacion.DoesNotExist:
            raise Http404("Poll does not exist")
    return render(request, './citaciones/anteriores.html', {"citaciones": obj, "current_datetime": current_datetime})
    
    
    