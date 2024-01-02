from django.http import HttpResponse
from django.shortcuts import render
from intranet.models import Licencia, Citacion
from django.http import Http404
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required, permission_required

@login_required
@permission_required('intranet.check_licencias')
def licencia_revisar(request):
    current_date = datetime.now().date()
    current_datetime = datetime.now()

    
    citaciones = Citacion.objects.filter(fecha__gt=current_date)
    

    return render(request, './licencias/revisar_admin.html', {"citaciones": citaciones, "current_datetime": current_datetime})
    
    
    