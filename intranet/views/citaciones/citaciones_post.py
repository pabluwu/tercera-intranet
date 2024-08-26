from django.shortcuts import render
from intranet.models import Citacion
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.utils.html import strip_tags
from django.core import mail
from django.core.mail import send_mail, EmailMultiAlternatives
from django.contrib.auth.models import User

from intranet.forms import CitacionForm

@login_required
@permission_required('intranet.add_citacion')
def citaciones_post(request):
    current_datetime = datetime.now()
    context = {"form": CitacionForm(), "current_datetime": current_datetime}

    if request.method == 'POST':
        formulario = CitacionForm(data=request.POST)
        if formulario.is_valid():
            new_citacion = formulario.save(commit=False)
            
            time_change = timedelta(hours=formulario.cleaned_data['hora'].hour, minutes=formulario.cleaned_data['hora'].minute)
            new_citacion.fecha = new_citacion.fecha+time_change
            new_citacion.save()
            
            
            #Inicio envío de correo
            users = User.objects.all()
            emails =[u.email for u in users]
            
            host = request.get_host()
            message_full = f"""
                <html>
                <p><strong>Se ha creado la siguiente citaci&oacute;n</strong></p>
                <p><strong>Nombre: </strong>{new_citacion.nombre}</p>
                <p><strong>Fecha: </strong>{new_citacion.fecha}</p>
                <p><strong>Tenida: </strong>{new_citacion.tenida}</p>
                <p><strong>Lugar: </strong>{new_citacion.lugar}</p>
                <p>Si no desea asistir puede dejar su licencia correspondiente haciendo click <strong> <a href="https://{host}/tercera/licencia/{new_citacion.id}">aqu&iacute;.</a></strong></p>
                </html>
            """
            plain_message = strip_tags(message_full)
            
            connection = mail.get_connection()
            connection.open()
            
            for e in emails:
                msg = EmailMultiAlternatives(
                    subject = "Nueva citación",
                    body = plain_message,
                    # from_email = "contacto@bombalandeta.cl",
                    from_email = "contact@terceraquillota.co.site",
                    to = [e,],
                    reply_to=["licencias.terceraquillota@gmail.com"],
                )
                
                msg.attach_alternative(message_full, "text/html")
                
                msg.send()
                
            connection.close()
            #Fin envío de correo
                
            messages.success(request, "Citación creada correctamente")
        else:
            context['form'] = formulario

    return render(request, './citaciones/post.html', context)
    
    
    