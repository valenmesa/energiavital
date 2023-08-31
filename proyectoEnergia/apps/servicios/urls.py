from  django.urls import re_path, include
from apps.servicios.views import index, serviciosList, serviciosCreate, serviciosEdit, serviciosDelete

urlpatterns = [
    # re_path(r'^$', index, name='index'),
    re_path(r'^editar/(?P<pk>\d+)/$', serviciosEdit.as_view(), name='servicios_editar'),
    re_path(r'^eliminar/(?P<pk>\d+)/$', serviciosDelete.as_view(), name='servicios_eliminar'),
    re_path(r'^nuevo$', serviciosCreate.as_view(), name='servicios_crear'),
    re_path(r'^listar$', serviciosList.as_view(), name='servicios_listar'),
    
]