from django.shortcuts import render
from django.http import HttpResponse
from apps.profesor.models import Profesor
from apps.profesor.form import ProfesorForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.
#Pagina inicial
def index(request):
    return render(request, "profesor/index.html")

class ProfesorList(ListView):
    model=Profesor
    template_name='profesor/profesor_list.html'

#crear registro
class ProfesorCreate(CreateView):
    model=Profesor
    form_class= ProfesorForm
    template_name='profesor/profesor_form.html'
    success_url= reverse_lazy('profesor_listar')

#Editar registro
class ProfesorEdit(UpdateView):
    model=Profesor
    form_class= ProfesorForm
    template_name='profesor/profesor_form.html'
    success_url= reverse_lazy('profesor_listar')

# Eliminar registro
class ProfesorDelete(DeleteView):
    model=Profesor
    template_name='profesor/profesor_delete.html'
    success_url= reverse_lazy('profesor_listar')