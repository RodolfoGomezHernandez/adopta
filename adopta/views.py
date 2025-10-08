from django.shortcuts import render, redirect
from .forms import ContactoForm # Importamos el formulario
from .models import Contacto, Mascota # Importamos los modelos
# Create your views here.
def home(request):
    #Esta vista renderiza la plantilla home.html cuando se accede a la ruta raíz
    return render(request, 'home.html')

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid(): # Verificamos que los datos sean correctos
            # Procesamos los datos del formulario
            datos = form.cleaned_data
            nuevo_contacto = Contacto(
                nombre=datos['nombre'],
                correo=datos['correo'],
                telefono=datos['telefono'],
                comuna=datos['comuna']
            )
            nuevo_contacto.save() # Guardamos en la base de datos
            
            # Redirigimos a la portada como 
            return redirect('home')
    else:
        form = ContactoForm()

    return render(request, 'contacto.html', {'form': form})

def lista_mascotas(request):
    # Obtenemos todos los objetos Mascota de la base de datos
    mascotas = Mascota.objects.all()
    # Pasamos las mascotas a la plantilla en un diccionario
    return render(request, 'lista_mascotas.html', {'mascotas': mascotas})

