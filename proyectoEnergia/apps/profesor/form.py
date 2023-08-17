from django import forms
from apps.profesor.models import Profesor

class ProfesorForm (forms.ModelForm):
    class Meta:
        model = Profesor
        fields = [
            'nombre_profesor',
            'apellido_profesor',
            'telefono_profesor',
            'email_profesor',
            'direccion_profesor',
            'tipo_documento',
            'numero_documento',
        ]
        labels ={
            'nombre_profesor': 'Nombre',
            'apellido_profesor': 'Apellido',
            'telefono_profesor': 'Telefono',
            'email_profesor': 'Email',
            'direccion_profesor':'Direccion',
            'tipo_documento':'Tipo de documento',
            'numero_documento': 'Numero de documento',
        }
        Widgets={
            'nombre_profesor': forms.TextInput(attrs={'class':'form-control'}),
            'apellido_profesor': forms.TextInput(attrs={'class':'form-control'}),
            'Telefono_profesor': forms.TextInput(attrs={'class':'form-control'}),
            'Email_profesor': forms.TextInput(attrs={'class':'form-control'}),
            'direccion_profesor': forms.TextInput(attrs={'class':'form-control'}),
            'tipo_documento': forms.Select(attrs={'class':'form-control'}),
            'numero_documento': forms.TextInput(attrs={'class':'form-control'}),
        }
    # def __init__(self, *args, **Kwargs):
    #     super().__init__(*args, **Kwargs)
    #     for field in iter(self.fields):
    #         self.fields[field].widget.attrs.update({
    #             'class':'form-control'
    #         })