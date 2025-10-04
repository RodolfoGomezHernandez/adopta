from django.shortcuts import render

# Create your views here.
def home(request):
    #Esta vista renderiza la plantilla home.html cuando se accede a la ruta raíz
    return render(request, 'home.html')