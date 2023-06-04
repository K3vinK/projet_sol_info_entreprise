from django.shortcuts import render, redirect
from computerApp.models import AddMachineForm, AddPersonForm, Machine
from computerApp.models import Personne
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def index(request) :
    machines = Machine.objects.all()
    context = {}
    return render(request, 'templates/index.html', context)

def machine_list_view(request):
    machine = Machine.objects.all()
    context= {'machines': machine}
    return render(request,'computerApp/machine_list.html', context)

def personne_list_view(request):
    personne = Personne.objects.all()
    context= {'personnes': personne}
    return render(request,'computerApp/personne_list.html', context)

def machine_detail_view(request, pk):
    machine = get_object_or_404(Machine, pk=pk)
    context = {'machine': machine}
    return render(request, 'computerApp/machine_detail.html', context)
 

def personne_detail_view(request, pk):
    personne = get_object_or_404(Personne, pk=pk)
    context = {'personne': personne}
    return render(request, 'computerApp/personne_detail.html', context)


def machine_add_form(request):
    if request.method == 'POST':
        form = AddMachineForm(request.POST or None)
        if form.is_valid():
            new_machine= Machine(nom=form.cleaned_data['nom'])
            new_machine.save()
            return redirect('machines')
    else:
        form = AddMachineForm()
    
    context = {'form': form}
    return render(request, 'computerApp/machine_add.html', context)


def person_add_form(request):
    if request.method == 'POST':
        form = AddPersonForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            new_person = Personne(nom=nom)  # Create a new Personne object, not Machine
            new_person.save()
            return redirect('personnes')
    else:
        form = AddPersonForm()
    
    context = {'form': form}
    return render(request, 'computerApp/personne_add.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, )
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, )
            return redirect('login')

def logout_user(request):
    logout(request)
    messages.success(request, ("You were deconnected"))
    return redirect('home')

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration successfull"))
            return redirect('home')
    return render(request, 'computerApp/register_user.html', {})
    return render(request, 'computerApp/personne_add.html', context)
