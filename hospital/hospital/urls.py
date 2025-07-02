"""hospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from planta import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home' ),
    path('registro/',views.registro, name='registro' ),
    path('login/',views.iniciar_sesion, name= 'login'),
    path('logout/',views.cerrar_sesion, name= 'logout'),
    path('plantas/',views.lista_plantas, name= 'lista_planta'),
    path('plantas/agregar/',views.agregar_planta, name= 'agregar_planta'),
    path('plantas/editar/<int:id>/',views.editar_planta, name= 'editar_planta'),
    path('plantas/eliminar/<int:id>/',views.eliminar_planta, name= 'eliminar_planta'),
    path('plantas/reporte/pdf/',views.generar_reporte_pdf, name='reporte_pdf'),
    path('plantas/dashboard/', views.dashboard_planta, name='dashboard_planta')
]
