from django.shortcuts import render, HttpResponse, redirect
from .models import FichaMantenimiento
from .forms import FichaFormulario
from django.contrib.auth.models import User, Group

# Create your views here.
def index(request):
    listaFichas = FichaMantenimiento.objects.all().order_by('dispositivo')
    return render(request,'fichasMantenimiento/principal.html', locals())
    return render(request,'fichasMantenimiento/principal.html')
    

def guardar(request):
    
    formulario_ficha = FichaFormulario(request.POST)
    if request.method == 'POST':
        if formulario_ficha.is_valid():
            ficha = FichaMantenimiento()
            datos_ficha = formulario_ficha.cleaned_data
            ficha.numero_ficha = datos_ficha.get('numero_ficha')
            ficha.dispositivo = datos_ficha.get('dispositivo')
            ficha.problema = datos_ficha.get('problema')
            ficha.fecha = datos_ficha.get('fecha')
            ficha.save()
            
            return redirect(index)
    return render(request, 'fichasMantenimiento/guiRegistrarFicha.html', locals())
