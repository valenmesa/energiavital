from  django.urls import re_path, include
from apps.profesor.views import index, ProfesorList, ProfesorCreate, ProfesorEdit, ProfesorDelete

urlpatterns = [
    re_path(r'^$', index, name='index'),
    re_path(r'^editar/(?P<pk>\d+)/$', ProfesorEdit.as_view(), name='profesor_editar'),
    re_path(r'^eliminar/(?P<pk>\d+)/$', ProfesorDelete.as_view(), name='profesor_eliminar'),
    re_path(r'^nuevo$', ProfesorCreate.as_view(), name='profesor_crear'),
    re_path(r'^listar$', ProfesorList.as_view(), name='profesor_listar'),
]