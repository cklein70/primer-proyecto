from django.shortcuts import render
from django.http import HttpResponse
from mi_familia.models import familia

def ingreso_familiar(request):
    nuevo_familiar = familia.objects.create(nombre="SEzequiel", parentezco="Tio", edad=31, estudia= False) 
    return HttpResponse("Se Ingreso el nuevo familiar")

def lista_familiares(request):
     familiares=familia.objects.all()
     print (familiares)
     context={
          "familia":familiares,   
     }
     return render(request,"lista_familiares.html", context = context)