from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import Mascota, Contacto
from .forms import ContactoForm, MascotaForm
# Create your views here.
def home(request):
    #Esta vista renderiza la plantilla home.html cuando se accede a la ruta raíz
    return render(request, 'adopta/home.html')

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

    return render(request, 'adopta/contacto.html', {'form': form})

def lista_mascotas(request):
    # Obtenemos todos los objetos Mascota de la base de datos
    mascotas = Mascota.objects.all()
    # Pasamos las mascotas a la plantilla en un diccionario
    return render(request, 'adopta/listar_mascotas.html', {'mascotas': mascotas})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'adopta/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

# Vistas del Dashboard (protegidas con @login_required) 
@login_required
def dashboard_view(request):
    return render(request, 'adopta/dashboard/dashboard_home.html')

@login_required
def mascotas_list_view(request):
    mascotas = Mascota.objects.all()
    return render(request, 'adopta/dashboard/mascotas_list.html', {'mascotas': mascotas})

@login_required
def interesados_list_view(request):
    interesados = Contacto.objects.all()
    return render(request, 'adopta/dashboard/interesados_list.html', {'interesados': interesados})

@login_required
def mascotas_create_view(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mascotas_list')
    else:
        form = MascotaForm()
    return render(request, 'adopta/dashboard/mascotas_form.html', {'form': form})

@login_required
def mascotas_update_view(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    if request.method == 'POST':
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
            return redirect('mascotas_list')
    else:
        form = MascotaForm(instance=mascota)
    return render(request, 'adopta/dashboard/mascotas_form.html', {'form': form})

@login_required
def mascotas_delete_view(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    if request.method == 'POST':
        mascota.delete()
        return redirect('mascotas_list')
    return render(request, 'adopta/dashboard/mascotas_confirm_delete.html', {'mascota': mascota})

