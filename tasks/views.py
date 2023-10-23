from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User as uu
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Task,Usuario, Post, Noticia, Proyecto, Institucion, BolsaTrabajoPost, AplicacionBolsaTrabajo
from django.contrib.auth import password_validation
from .forms import TaskForm,RegisterUserForm,LoginUserForm,NoticiaForm
from django import forms
from django.shortcuts import render
# Create your views here.


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {"form": RegisterUserForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                
                User = uu.objects.create_user(
                    username=request.POST["username"],email=request.POST["email"],password=request.POST["password1"],first_name=request.POST["first_name"],last_name=request.POST["last_name"])
                password_validation.validate_password(request.POST["password1"], User)
                User.save()
                login(request, User)
                return redirect('userhome')
            except IntegrityError:
                return render(request, 'signup.html', {"form": RegisterUserForm, "error": "Ese usuario ya existe."})
            except forms.ValidationError:
                return render(request, 'signup.html', {"form": RegisterUserForm, "error": "Contraseña no cumple requisitos."})

        return render(request, 'signup.html', {"form": RegisterUserForm, "error": "Las contraseñas no coinciden."})

@login_required
def userhome(request):
    #tasks = Task.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'userhome.html')

@login_required
def tasks(request):
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'tasks.html', {"tasks": tasks})

@login_required
def noticias(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticias.html', {"noticias": noticias})

@login_required
def tasks_completed(request):
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'tasks.html', {"tasks": tasks})


@login_required
def create_task(request):
    if request.method == "GET":
        return render(request, 'create_task.html', {"form": TaskForm})
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'create_task.html', {"form": TaskForm, "error": "Error creating task."})

@login_required
def crear_noticia(request):
    if request.method == "GET":
        return render(request, 'crear_noticia.html', {"form": NoticiaForm})
    else:
        try:
            form = NoticiaForm(request.POST, request.FILES)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('crear_noticia')
        except ValueError:
            return render(request, 'crear_noticia.html', {"form": NoticiaForm, "error": "Error al publicar noticias."})


def home(request):
    return render(request, 'home.html')

def registrar(request):
    return render(request, 'registrar.html')

def userhome(request):
    return render(request, 'userhome.html')
    

@login_required
def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {"form": LoginUserForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {"form": LoginUserForm, "error": "Usuario o contraseña incorrecta."})

        login(request, user)
        return redirect('crear_noticia')

@login_required
def task_detail(request, task_id):
    if request.method == 'GET':
        task = get_object_or_404(Task, pk=task_id, user=request.user)
        form = TaskForm(instance=task)
        return render(request, 'task_detail.html', {'task': task, 'form': form})
    else:
        try:
            task = get_object_or_404(Task, pk=task_id, user=request.user)
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'task_detail.html', {'task': task, 'form': form, 'error': 'Error updating task.'})

@login_required
def noticia_detalle(request, id_noticias):
    if request.method == 'GET':
        noticia = get_object_or_404(Noticia, pk=id_noticias, user=request.user)
        form = NoticiaForm(instance=noticia)
        return render(request, 'noticia_detalle.html', {'noticia': noticia, 'form': form})
    else:
        try:
            noticia = get_object_or_404(Noticia, pk=id_noticias, user=request.user)
            form = NoticiaForm(request.POST, instance=noticia)
            form.save()
            return redirect('noticias')
        except ValueError:
            return render(request, 'noticia_detalle.html', {'noticia': noticia, 'form': form, 'error': 'Error updating noticia.'})


@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.save()
        return redirect('tasks')

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')
    
@login_required
def borrar_noticia(request, id_noticias):
    noticia = get_object_or_404(Noticia, pk=id_noticias, user=request.user)
    if request.method == 'POST':
        noticia.delete()
        return redirect('noticias')