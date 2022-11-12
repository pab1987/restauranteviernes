from django.shortcuts import render
from web.formularios.formularioPlatos import FormularioRegistroPlatos
from web.formularios.formularioEmpleados import FormularioRegistroEmpleados

# Create your views here.

#CADA VISTA ES UNA FUNCION DE PY

def Home(request):
    return render(request,'index.html')

def Platos(request):

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
            print(datosLimpios)

    return render(request,'platos.html',diccionarioEnvioDatos)

def Empleados(request):
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
            print(datosLimpios)

    return render(request,'empleados.html',diccionarioEnvioDatosEmpleados)