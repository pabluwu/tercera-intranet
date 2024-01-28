from django.http import FileResponse
from intranet.models import Cuota
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required


@login_required
def list_cuota(request):
    context = {}
    
    cuota = Cuota.objects.filter(user=request.user)
    
    meses = cuota[0].Mes
    
    cuotas={}
    
    for mes in cuota[0].Mes:
        for c in cuota:    
            if c.mes == mes.value:
                cuotas[mes.label] = c
            else:
                cuotas[mes.label] = 'empty'
    
    context['cuotas'] = cuotas
    print(cuotas['Enero'].mes)
    
    return render(request, './cuota/list.html', context)