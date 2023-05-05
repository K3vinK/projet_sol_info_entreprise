from django.shortcuts import render
from computerApp.models import Machine
from computerApp.models import Personne
from computerApp.models import get_object_or_404

def index(request) :
    machines = Machine.objects.all()
    context = {}
    return render(request, 'templates/index.html', context)

def machine_list_view(request):
    machine = Machine.objects.all()
    context= {'machines': machine}
    return render(request,
    'computerApp/machine_list.html', 
    context)

def personne_list_view(request):
    personne = Personne.objects.all()
    context= {'personnes': personne}
    return render(request,'computerApp/personne_list.html', context)

def machine_detail_view(request, pk):
    machine = get_object_or_404(Machine, id=pk)
    context={'machines': machine}
    return render(request,
        'computerApp/machine_detail.html',
        context)

def personne_detail_view(request, st):
    personne = get_object_or_404(Personne, id=st)
    context={'personnes': personne}
    return render(request,
        'computerApp/personne_detail.html',
        context)        