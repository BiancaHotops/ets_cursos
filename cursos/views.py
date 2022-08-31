from django.shortcuts import render
from .models import Cursos
#from django.http import HttpResponse

def index(request):
    return render (request,'index.html')
    #return HttpResponse('<H1> Cursos ETS </h1>')
    
def cursos(request):
    return render (request, 'curso.html')

# Create your views here.

def index(request):
    
    # cursos={
    #     1: 'Smart Automation',
    #     2: 'Mecatrônica',
    #     3: 'Manufatura Digital',
    #     4: 'Administração'
    # }

    cursos = Cursos.objects.all()

    
    dados = {
        'cursos' : cursos
    }
    
    return render(request, 'index.html', dados)


