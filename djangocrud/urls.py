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
from django.contrib.auth import views as auth_views

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
    path('publicacion/<int:id_noticias>', views.Pub_detalle, name='noticia_detallepub'),
    path('noticias/<int:id_noticias>/borrar', views.borrar_noticia, name='borrar_noticia'),
    path('ver_noticia/<int:id_noticias>', views.ver_noticia, name='ver_noticia'),
    path('set/', views.set, name="set"),
    path('publicaciones/', views.publicacion, name='publicacion'),
    path('ver_publicación/<int:id_noticias>', views.ver_publicacion, name='ver_publicacion'),
    path('crear_publicacion/', views.crear_publicacion, name='crear_publicacion'),
    path('buscar_noticias/', views.buscar_noticias, name='buscar_noticias'),
    path('facilities/', views.facil, name='facilities'),
    path('facilities1/', views.facil1, name='facilities1'),
    path('facilities3/', views.facil3, name='facilities3'),
    path('user_public_view/<int:id_user>', views.user_public_view, name='user_public_view'),
    path('equipo/', views.equipo, name='equipo'),
    path('contacto/', views.contacto_view, name='contacto'),
    
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset_password/<uid64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
     path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
