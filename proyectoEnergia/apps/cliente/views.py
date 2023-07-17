from django.shortcuts import render
from django.http import HttpResponse
from apps.cliente.models import Cliente
from apps.cliente.form import ClienteForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.
#Pagina inicial
def index(request):
    return render(request, "profesor/index.html")

class ClienteList(ListView):
    model=Cliente
    template_name='cliente/cliente_list.html'
    paginate_by= 2

#crear registro
class ClienteCreate(CreateView):
    model=Cliente
    form_class= ClienteForm
    template_name='cliente/cliente_form.html'
    success_url= reverse_lazy('cliente_listar')

#Editar registro
class ClienteEdit(UpdateView):
    model=Cliente
    form_class= ClienteForm
    template_name='cliente/cliente_form.html'
    success_url= reverse_lazy('cliente_listar')

# Eliminar registro
class ClienteDelete(DeleteView):
    model=Cliente
    template_name='cliente/cliente_delete.html'
    success_url= reverse_lazy('cliente_listar')
