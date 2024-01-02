from django.http import HttpResponse
from django.shortcuts import render
from intranet.models import Licencia, Citacion
from django.http import Http404
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required

@login_required
def licencia_list_historico(request):

    current_date = datetime.now().date()
    current_datetime = datetime.now()

    licencias = Licencia.objects.filter(autor_id=request.user.id).order_by('-fecha_licencia')
    obj = []
    context = {"licencias": obj, "current_datetime": current_datetime}
    for l in licencias:
        print(current_datetime)
        try:
            c = Citacion.objects.get(id=l.citacion_id)
            obj.append({'licencia':l,'citacion':c})
            context['empty'] = False
        except Citacion.DoesNotExist:
            context['empty'] = True

    

    return render(request, './licencias/list_historico.html', context)
    
    
    