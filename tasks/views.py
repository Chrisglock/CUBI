from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Task,Usuario, Post, Noticia, Proyecto, Institucion, BolsaTrabajoPost, AplicacionBolsaTrabajo
from django.contrib.auth import password_validation
from .forms import TaskForm,RegisterUserForm,LoginUserForm,NoticiaForm,UserForm,PerfilUsuario
from django import forms
from django.core.files.storage import default_storage
# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            if form.cleaned_data["password1"] == form.cleaned_data["password2"]:
                try:
                    user = User.objects.create_user(
                        username=form.cleaned_data["username"],
                        email=form.cleaned_data["email"],
                        password=form.cleaned_data["password1"],
                        first_name=form.cleaned_data["first_name"],
                        last_name=form.cleaned_data["last_name"]
                    )
                    login(request, user)
                    return redirect('crear_noticia') 
                except IntegrityError:
                    return render(request, 'signup.html', {"form": form, "error": "El nombre de usuario o correo electrónico ya está en uso. Por favor, elige otro."})
            else:
                return render(request, 'signup.html', {"form": form, "error": "Las contraseñas no coinciden."})
        else:
            return render(request, 'signup.html', {"form": form, "error": "El formulario no es válido."})
    else:
        form = RegisterUserForm()
        return render(request, 'signup.html', {"form": form})

def set(request):
    user_profile = PerfilUsuario.objects.get(user=request.user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            # Verificar si hay una imagen asociada y eliminarla si existe
            if user_profile.imagen_perfil:
                # Guardar la ruta del archivo a eliminar
                file_path = user_profile.imagen_perfil.path
                # Eliminar la imagen antigua del sistema de archivos
                default_storage.delete(file_path)
            form.save()
            return redirect('userhome')  # Redirigir a la página de inicio o a donde desees
    else:
        form = UserForm(instance=user_profile)

    context = {'form': form}
    return render(request, 'set.html', context)

@login_required
def tasks(request):
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'tasks.html', {"tasks": tasks})


def noticias(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticias.html', {"noticias": noticias})

@login_required
def editar_noticias(request):
    noticias = Noticia.objects.all()
    return render(request, 'editar_noticias.html', {"noticias": noticias})

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
    user_profile = PerfilUsuario.objects.get(user=request.user)
    form = UserForm(instance=user_profile)
    context = {
       'form': form,
       "form_not": NoticiaForm,
   }
    if request.method == "GET":
        return render(request, 'crear_noticia.html', context)
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
    user_profile = PerfilUsuario.objects.get(user=request.user)
    form = UserForm(instance=user_profile)
    context = {'form': form}
    return render(request, 'userhome.html',context)

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
    user_profile = PerfilUsuario.objects.get(user=request.user)
    if request.method == 'GET':
        noticia = get_object_or_404(Noticia, pk=id_noticias, user=request.user)
        form = NoticiaForm(instance=noticia)
        return render(request, 'noticia_detalle.html', {'noticia': noticia, 'form': form})
    else:
        try:
            noticia = get_object_or_404(Noticia, pk=id_noticias, user=request.user)
            form = NoticiaForm(request.POST,request.FILES, instance=noticia)
            print(request.FILES)
            form.save()
            return redirect('editar_noticias')
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
        return redirect('editar_noticias')
    
def ver_noticia(request, id_noticias):
    noticia = get_object_or_404(Noticia, id_noticias=id_noticias)
    return render(request, 'ver_noticia.html', {'noticia': noticia})