from django.http import FileResponse
from intranet.models import Cuota
from intranet.forms import CuotaForm
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required


@login_required
def post_cuota(request):
    context = { 'form' : CuotaForm() }
    
    
    
    
    return render(request, './cuota/ingreso.html', context)