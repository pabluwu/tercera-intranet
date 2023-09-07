from django.shortcuts import render
from intranet.forms import LicenciaForm

def post_licencia(request):

    context = { 'form' : LicenciaForm() }
    return render(request, './licencias/post.html', context)