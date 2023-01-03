from django.shortcuts import render
from django.http import HttpResponse
from mi_familia.models import familia

def ingreso_familiar(request,nombre,parentezco,edad,estudia):
     if estudia == 0:
          estudia=False     
     else:
       estudia =True      
     nuevo_familiar = familia.objects.create(nombre= nombre, parentezco= parentezco, edad= edad, estudia= estudia) 
     return HttpResponse(f"Se Ingreso el nuevo familiar: {nombre}")


def lista_familiares(request):
     familiares=familia.objects.all()
     print (familiares)
     context={
          "familia":familiares,   
     }
     return render(request,"lista_familiares.html", context = context)