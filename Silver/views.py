

from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context


def inicio(request):
    return HttpResponse("Hola Iraís")

def ver_fecha(request):
    fecha_actual = datetime.now()
    return HttpResponse(f"Fecha actual:{fecha_actual}")

def saludo(request, nombre, apellido):
    return HttpResponse(f"<h1> Hola {nombre}{apellido}</h1>")
    

def mi_template(request):
    
    archivo = open(r"C:\Users\DavidFernandoRodrigu\Desktop\Silverteam\templates\prueba.html", "r")
    
    template1 = Template(archivo.read())
    
    contexto1 = Context()
    
    render1 = template1.render(contexto1)
    
    return HttpResponse(render1) 