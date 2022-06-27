

from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader

from primerasvistas.models import Perro



def inicio(request):
    return HttpResponse("Hola Iraís")

def ver_fecha(request):
    fecha_actual = datetime.now()
    return HttpResponse(f"Fecha actual:{fecha_actual}")

def saludo(request, nombre, apellido):
    return HttpResponse(f"<h1> Hola {nombre}{apellido}</h1>")
    

#v1
#def mi_template(request):
    
#    archivo = open(r"C:\Users\DavidFernandoRodrigu\Desktop\Silverteam\templates\prueba.html", "r")
    
#    template1 = Template(archivo.read())
    
#    archivo.close()
    
#    nombre = "Fernando Gijon"
    
#    contexto1 = Context({"nombre" : nombre})
    
#    render1 = template1.render(contexto1)
    
#    return HttpResponse(render1)





#v2

def mi_template(request):
    
    
    
    template1 = loader.get_template("prueba.html")
    
    nombre = "Fernando"
    apellido = "Gijon"
    
    lista = ["Katia", "Maximo Decimo", "Esme", "Memo", "Memito", "Brisa", "Nemo"]
    
    
    perro = Perro(nombre="Fernando", edad=31) 
    perro2 = Perro(nombre="David", edad=31) 
    perro3 = Perro(nombre="Fercho", edad=31) 
    
    render1 = template1.render(
        {"nombre" : nombre, "apellido" : apellido, "edad" : 6000, "lista": lista , "perro": perro 
         , "perro2": perro2, "perro3": perro3})
    
    return HttpResponse(render1)