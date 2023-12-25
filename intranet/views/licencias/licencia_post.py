from django.shortcuts import render
from intranet.forms import LicenciaForm
from intranet.models import Citacion, Licencia
from django.shortcuts import get_object_or_404
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, reverse


current_date = datetime.now().date()
current_datetime = datetime.now()


@login_required
def post_licencia(request, id):
    
    citacion = get_object_or_404(Citacion, id=id)

    context = { 'form' : LicenciaForm(), 'citacion' : citacion }

    #Flag para bloquear licencia si se pasa de 24 horas.
    flag = False
    time_difference = citacion.fecha - current_datetime


    if time_difference >= timedelta(hours=24):
        flag = True

        _vals = {'citacion_id': id, 'autor_id':request.user.id}
        licencia = Licencia.objects.filter(**_vals)

        if licencia:
            context['licencia'] = licencia[0]
        if request.method == 'POST':
            formulario = LicenciaForm(data=request.POST)

            #Check if Licencia exists.
            
            if not licencia:
                if formulario.is_valid():
                    new_licencia = formulario.save(commit=False)
                    new_licencia.citacion_id = id
                    new_licencia.autor_id = request.user.id
                    new_licencia.save()
                    context['message'] = 'Licencia enviada exitosamente.'
                    return redirect(reverse('post_licencia', args=(id,)))
                else:
                    context['form'] = formulario
            else:
                context['licencia'] = licencia[0]
                
    context['flag'] = flag
    return render(request, './licencias/post.html', context)