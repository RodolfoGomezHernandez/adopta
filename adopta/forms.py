from django import forms

class ContactoForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100, required=True)
    correo = forms.EmailField(label='Correo', required=True)
    telefono = forms.CharField(label='Teléfono', max_length=15, required=True)
    comuna = forms.CharField(label='Comuna', max_length=100, required=True)