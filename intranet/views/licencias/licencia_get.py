from django.shortcuts import render
from intranet.models import Citacion, Licencia
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


@login_required
def get_licencia(request, id):
    
    licencia = get_object_or_404(Licencia, id=id)
    citacion = get_object_or_404(Citacion, id = licencia.citacion_id)
    
    print(licencia)

    context = { 'licencia' : licencia, 'citacion' : citacion }

    return render(request, './licencias/get.html', context)