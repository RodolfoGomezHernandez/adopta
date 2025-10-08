from django import forms
from .models import Mascota # Importamos el modelo Mascota

class ContactoForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100, required=True)
    correo = forms.EmailField(label='Correo', required=True)
    telefono = forms.CharField(label='Teléfono', max_length=15, required=True)
    comuna = forms.CharField(label='Comuna', max_length=100, required=True)

#Formulario para crear y editar mascotas 
class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        # Excluimos el código porque es autoincremental
        fields = ['nombre', 'raza', 'peso', 'estatura', 'descripcion', 'region', 'comuna']