from django.shortcuts import render

# Create your views here.
from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppTerceraEntrega.models import Curso, Profesor
from AppTerceraEntrega.forms import CursoFormulario, ProfesorFormulario

# Create your views here.

def curso(request):

      curso =  Curso(nombre="Desarrollo web", camada="19881")
      curso.save()
      documentoDeTexto = f"--->Curso: {curso.nombre}   Camada: {curso.camada}"


      return HttpResponse(documentoDeTexto)


def inicio(request):

      return render(request, "AppTerceraEntrega/inicio.html")



def estudiantes(request):

      return render(request, "AppTerceraEntrega/estudiantes.html")


def entregables(request):

      return render(request, "AppTerceraEntrega/entregables.html")


def cursos(request):

      if request.method == 'POST':

            miFormulario = CursoFormulario(request.POST) 

            print(miFormulario)

            if miFormulario.is_valid:   

                  informacion = miFormulario.cleaned_data

                  curso = Curso (nombre=informacion['curso'], camada=informacion['camada']) 

                  curso.save()

                  return render(request, "AppTerceraEntrega/inicio.html")

      else: 

            miFormulario= CursoFormulario() 

      return render(request, "AppTerceraEntrega/cursos.html", {"miFormulario":miFormulario})




def profesores(request):

      if request.method == 'POST':

            miFormulario = ProfesorFormulario(request.POST) 

            print(miFormulario)

            if miFormulario.is_valid:   

                  informacion = miFormulario.cleaned_data

                  profesor = Profesor (nombre=informacion['nombre'], apellido=informacion['apellido'],
                   email=informacion['email'], profesion=informacion['profesion']) 

                  profesor.save()

                  return render(request, "AppTerceraEntrega/inicio.html") 

      else: 

            miFormulario= ProfesorFormulario() 

      return render(request, "AppTerceraEntrega/profesores.html", {"miFormulario":miFormulario})






def buscar(request):
    if request.GET["camada"]:
        camada = request.GET['camada'] 
        cursos = Curso.objects.filter(camada__icontains=camada)
        return render(request, "AppTerceraEntrega/inicio.html", {"cursos": cursos, "camada": camada})
    else: 
        respuesta = "No enviaste datos"
    # No olvidar from django.http import HttpResponse
    return HttpResponse(respuesta)