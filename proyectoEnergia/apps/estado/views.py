from django.shortcuts import render
from django.http import HttpResponse
from apps.estado.models import Estado
from apps.estado.form import EstadoForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
#Pagina inicial
def index(request):
    return render(request, "profesor/index.html")

class EstadoList(ListView):
    model=Estado
    template_name='estado/estado_list.html'
    paginate_by= 2
#crear registro
class EstadoCreate(CreateView):
    model=Estado
    form_class= EstadoForm
    template_name='estado/estado_form.html'
    success_url= reverse_lazy('estado_listar')

#Editar registro
class EstadoEdit(UpdateView):
    model=Estado
    form_class= EstadoForm
    template_name='estado/estado_form.html'
    success_url= reverse_lazy('estado_listar')

# Eliminar registro
class EstadoDelete(DeleteView):
    model=Estado
    template_name='estado/estado_delete.html'
    success_url= reverse_lazy('estado_listar')
