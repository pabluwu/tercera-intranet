from django.urls import path
from .views import citaciones_list
from .views import post_licencia
from intranet import views

urlpatterns = [
    path("citaciones", citaciones_list, name="citaciones_list"),

    path('licencia', post_licencia, name='post_licencia'),
]