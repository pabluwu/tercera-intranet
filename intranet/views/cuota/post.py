from django.http import FileResponse
from intranet.models import Cuota
from intranet.forms import CuotaForm
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def post_cuota(request):
    context = { 'form' : CuotaForm() }
    
    if request.method == 'POST':
        form = CuotaForm(request.POST)
        
        if form.is_valid():
            
            cuota_guardada = form.save(commit=False)
            
            cuota = Cuota.objects.filter(user=cuota_guardada.user, mes=cuota_guardada.mes)
            
            if not cuota: 
                form.save(commit=True)
                messages.success(request, "Cuota pagada correctamente")
            else:
                context['form'] = form
                messages.error(request, "Cuota ya se encuentra registrada")            
        else:
            context['form'] = form
    
    return render(request, './cuota/ingreso.html', context)