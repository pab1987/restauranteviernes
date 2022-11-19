from django.shortcuts import render
from web.formularios.formularioPlatos import FormularioRegistroPlatos
from web.formularios.formularioEmpleados import FormularioRegistroEmpleados

from web.models import Platos, Empleados

# Create your views here.

#CADA VISTA ES UNA FUNCION DE PY

def Home(request):
    return render(request,'index.html')

def PlatosVista(request):

    #cargar el formulario de registro de platos
    #Instanciar la clase
    formulario=FormularioRegistroPlatos()

    #creamos un diccionario para enviar datos hacia el template
    diccionarioEnvioDatos={
        'formulario':formulario
    }

    #Recibir información del formulario
    #Petición de tipo post
    if request.method=="POST":
        datosFormulario=FormularioRegistroPlatos(request.POST)
        if datosFormulario.is_valid():
            datosLimpios=datosFormulario.cleaned_data
            #ENVIANDO DATOS A MI BASE DE DATOS
            platoNuevo=Platos(
                nombre=datosLimpios["nombrePlato"],
                descripcion=datosLimpios["descripcionPlato"],
                imagen=datosLimpios["fotoPlato"],
                precio=datosLimpios["precioPlato"],
                tipo=datosLimpios["tipoPlato"]
            )
            platoNuevo.save()

    return render(request,'platos.html',diccionarioEnvioDatos)

def EmpleadosVista(request):
    #cargar el formulario de registro de empleados
    #Instanciar la clase
    formulario=FormularioRegistroEmpleados()

    #creamos un diccionario para enviar datos hacia el template
    diccionarioEnvioDatosEmpleados={
        'formularioEmleados':formulario
    }

    #Recibir información del formulario
    #Petición de tipo post
    if request.method=="POST":
        datosFormulario=FormularioRegistroEmpleados(request.POST)
        if datosFormulario.is_valid():
            datosLimpios=datosFormulario.cleaned_data
            #ENVIANDO DATOS A MI BASE DE DATOS
            empleadoNuevo=Empleados(
                nombre=datosLimpios["nombreEmpleado"],
                apellido=datosLimpios["apellidoEmpleado"],
                direccion=datosLimpios["direccionEmpleado"],
                documento=datosLimpios["documentoEmpleado"],
                rol=datosLimpios["rolEmpleado"]
            )
            empleadoNuevo.save()

    return render(request,'empleados.html',diccionarioEnvioDatosEmpleados)