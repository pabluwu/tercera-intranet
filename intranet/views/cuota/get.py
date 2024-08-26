from django.http import FileResponse
from intranet.models import Cuota
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required


@login_required
def list_cuota(request):
    context = {}
    
    cuota = Cuota.objects.filter(user=request.user)
    cuotas={
            'Enero' : 'empty',
            'Febrero' : 'empty',
            'Marzo' : 'empty',
            'Abril' : 'empty',
            'Mayo' : 'empty',
            'Junio' : 'empty',
            'Julio' : 'empty',
            'Agosto' : 'empty',
            'Septiembre' : 'empty',
            'Octubre' : 'empty',
            'Noviembre' : 'empty',
            'Diciembre' : 'empty'
        }
    if cuota:
        print(cuota)
        
        meses = cuota[0].Mes
        
        print(meses)
        
        
        
        for mes in cuota[0].Mes:
            for c in cuota:   
                print(mes.value, '/', c.mes)
                print(c.mes == mes.value)
                if c.mes == mes.value:
                    cuotas[mes.label] = c
        
        print(cuotas)
    context['cuotas'] = cuotas
    
    return render(request, './cuota/list.html', context)