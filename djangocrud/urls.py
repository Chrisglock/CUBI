"""djangocrud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from tasks import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks_completed/', views.tasks_completed, name='tasks_completed'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('create_task/', views.create_task, name='create_task'),
    path('tasks/<int:task_id>', views.task_detail, name='task_detail'),
    path('taks/<int:task_id>/complete', views.complete_task, name='complete_task'),
    path('tasks/<int:task_id>/delete', views.delete_task, name='delete_task'),
    path('registrar/', views.registrar, name='registrar'),
    path('userhome/', views.userhome, name='userhome'),
    path('crear_noticia/', views.crear_noticia, name='crear_noticia'),
    path('noticias/', views.noticias, name='noticias'),
    path('editar_noticias/', views.editar_noticias, name='editar_noticias'),
    path('noticias/<int:id_noticias>', views.noticia_detalle, name='noticia_detalle'),
    path('noticias/<int:id_noticias>/borrar', views.borrar_noticia, name='borrar_noticia'),
    path('ver_noticia/<int:id_noticias>', views.ver_noticia, name='ver_noticia'),
    path('set/', views.set, name="set"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
