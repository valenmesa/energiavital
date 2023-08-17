from django.shortcuts import render
from django.http import HttpResponse
from apps.profesor.models import Profesor
from apps.profesor.form import ProfesorForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic


# Create your views here.
#Pagina inicial
def index(request):
    return render(request, "profesor/index.html")

class ProfesorList(LoginRequiredMixin, generic.ListView):
    model=Profesor
    template_name='profesor/profesor_list.html'
    context_object_name="obj"
    login_url="login"

#crear registro
class ProfesorCreate(LoginRequiredMixin, generic.CreateView):
    model=Profesor
    form_class= ProfesorForm
    context_object_name="obj"
    template_name='profesor/profesor_form.html'
    success_url= reverse_lazy('profesor_listar')
    login_url="login"

    def form_valid(self, form):
        form.instance.uc=self.request.user
        return super().form_valid(form)

#Editar registro
class ProfesorEdit(LoginRequiredMixin, generic.UpdateView):
    model=Profesor
    form_class= ProfesorForm
    template_name='profesor/profesor_form.html'
    context_object_name="obj"
    success_url= reverse_lazy('profesor_listar')
    login_url="login"

    def form_valid(self, form):
        form.instance.um=self.request.user.id
        return super().form_valid(form)


# Eliminar registro
class ProfesorDelete(LoginRequiredMixin, generic.DeleteView):
    model=Profesor
    template_name='profesor/profesor_delete.html'
    context_object_name="obj"
    success_url= reverse_lazy('profesor_listar')