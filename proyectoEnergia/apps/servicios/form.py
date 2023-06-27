from django import forms
from apps.servicios.models import servicios

class serviciosForm (forms.ModelForm):
    class Meta:
        model = servicios
        fields = [
            'Nombre_Servicio',
            'Descripcion_Servicio',
            'Valor_Servicio',
        ]
        labels={
            'Nombre_Servicio':'Nombre',
            'Descripcion_Servicio':'Descripcion',
            'Valor_Servicio':'Valor',
        }
        widgets={
            'Nombre_Servicio':forms.TextInput(attrs={'class':'form-control'}),
            'Descripcion_Servicio':forms.Textarea(attrs={'class':'form-control'}),
            'Valor_Servicio':forms.TextInput(attrs={'class':'form-control'}),
        }