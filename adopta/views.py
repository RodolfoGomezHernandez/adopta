from django.shortcuts import render
from .forms import ContactoForm # Importamos el formulario
# Create your views here.
def home(request):
    #Esta vista renderiza la plantilla home.html cuando se accede a la ruta raíz
    return render(request, 'home.html')

def contacto(request):
    if request.method == 'POST':
        # Si el método es POST, se enviaron datos
        form = ContactoForm(request.POST)
        if form.is_valid():
            # El formulario es válido, podemos procesar los datos
            # Aquí iría la lógica para guardar en la BD o enviar un correo
            # Por ahora, solo redirigimos a la portada.
            return redirect('home')
    else:
        # Si el método es GET, solo mostramos el formulario vacío
        form = ContactoForm()

    return render(request, 'contacto.html', {'form': form})