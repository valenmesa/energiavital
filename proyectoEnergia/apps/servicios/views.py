from django.shortcuts import render
from django.http import HttpResponse
from apps.servicios.models import servicios
from apps.servicios.form import serviciosForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.
def index(request):
    return HttpResponse('Index servicio')


class serviciosList(ListView):
    model=servicios
    template_name='servicios/servicios_list.html'

#crear registro
class serviciosCreate(CreateView):
    model=servicios
    form_class= serviciosForm
    template_name='servicios/servicios_form.html'
    success_url= reverse_lazy('servicios_listar')

#Editar registro
class serviciosEdit(UpdateView):
    model=servicios
    form_class= serviciosForm
    template_name='servicios/servicios_form.html'
    success_url= reverse_lazy('servicios_listar')

# Eliminar registro
class serviciosDelete(DeleteView):
    model=servicios
    template_name='servicios/servicios_delete.html'
    success_url= reverse_lazy('servicios_listar')
