from django.shortcuts import render,redirect
from .models import Planta
from .forms import PlantaForm, RegistroUsuarioForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template  # Importa la función para cargar plantillas
from xhtml2pdf import pisa  # Importa la librería para generar PDFs
from django.http import HttpResponse  # Importa la clase HttpResponse
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

def generar_reporte_pdf(request):
    plantas = Planta.objects.all()  # Obtiene todos los productos
    template_path = 'planta/reporte_pdf.html'  # Ruta de la plantilla HTML para el PDF
    context = {'plantas': plantas}  # Contexto con los productos
    response = HttpResponse(content_type='application/pdf')  # Crea una respuesta HTTP con tipo PDF
    response['Content-Disposition'] = 'attachment; filename="reporte_productos.pdf"'  # Define el nombre del archivo PDF

    template = get_template(template_path)  # Carga la plantilla
    html = template.render(context)  # Renderiza la plantilla con el contexto

    pisa_status = pisa.CreatePDF(html, dest=response)  # Genera el PDF a partir del HTML
    if pisa_status.err:  # Si hay error al generar el PDF
        return HttpResponse('Hubo un error al generar el PDF', status=500)  # Devuelve un error
    return response  # Devuelve el PDF generado

@login_required  # Requiere que el usuario esté autenticado
def dashboard_planta(request):
    plantas = Planta.objects.all()  # Obtiene todos las plantas
    nombres = [p.nombre for p in plantas]  # Lista de nombres de plantas
    nroCamas = [[float(p.numeroCamas) for p in plantas]]  # Lista de numero de camas de planta
    return render(request, 'planta/dashboard.html', {
        'labels': nombres,  # Pasa los nombres como etiquetas
        'data': nroCamas  # Pasa los numeros de camas como datos
    })

