from django.shortcuts import render,redirect
from .models import Planta
from .forms import PlantaForm, RegistroUsuarioForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request, 'home.html')


def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'registro.html', {'form':form})

def iniciar_sesion(request):
    if request.method == 'POST':
        usuario = request.POST['username']
        clave = request.POST['password']
        user = authenticate(request, username=usuario, password=clave)

        if user:
            login(request, user)
            return redirect('lista_planta')
    return render(request, 'login.html')


def cerrar_sesion(request):
    logout(request)
    return redirect('login')


@login_required
def lista_plantas(request):
    plantas = Planta.objects.all()
    return render(request, 'planta/lista.html', {'plantas':plantas})

@login_required
def agregar_planta(request):
    form= PlantaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_planta')
    return render(request, 'planta/form.html', {'form':form})

@login_required
def editar_planta(request,id):
    planta = Planta.objects.get(id=id)
    form = PlantaForm(request.POST or None, instance=planta)
    if form.is_valid():
        form.save()
        return redirect('lista_planta')
    return render(request, 'planta/form.html', {'form':form})

@login_required
def eliminar_planta(request,id):
    planta= Planta.objects.get(id=id)
    planta.delete()
    return redirect('lista_planta')