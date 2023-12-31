from django.http import HttpResponse
from django.shortcuts import render
from intranet.models import Citacion
from django.http import Http404
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required

@login_required
def citaciones_list(request):
    current_date = datetime.now().date()
    current_datetime = datetime.now()
    try:
        citaciones = Citacion.objects.filter(fecha__gt=current_date)
        objs = []
        for obj in citaciones:
            flag = False
            time_difference = obj.fecha - current_datetime
            if obj.fecha < current_datetime:
                continue

            if time_difference >= timedelta(hours=24):
                flag = True
            objs.append({"obj":obj,"flag":flag}) 
        print(objs)
    except Citacion.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, './citaciones/index.html', {"citaciones": objs, "current_datetime": current_datetime})
    
    
    