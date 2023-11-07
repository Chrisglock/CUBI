from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.files import ImageField 
from django.utils import timezone
from ckeditor.fields import RichTextField
# Create your models here.
def default_profile_image():
    return "media/profile.png"


class Usuario(models.Model):
    id_user = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    descripcion = models.TextField()
    social_media_link = models.TextField()
    alumno = models.BooleanField()
    imagen_perfil = models.ImageField(default="profile.png", null=True, blank=True)
    admin = models.BooleanField()
    institucion_id = models.ForeignKey('Institucion', on_delete=models.CASCADE, default=0,blank=True)
    def __str__(self) -> str:
        return self.nombre  

 # Modelo de Perfil
class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255, null=True)
    email = models.EmailField(null=True)
    descripcion = models.TextField(null=True)
    Linkedin = models.URLField(null=True, blank=True)
    Twitter = models.URLField(null=True, blank=True)
    Instagram = models.URLField(null=True, blank=True)
    alumno = models.BooleanField(null=True, default=False)
    imagen_perfil = models.ImageField(null=True,default="profile.png")
    admin = models.BooleanField(null=True, default=False)

    def __str__(self):
        return self.nombre
# Modelo de Posts
class Post(models.Model):
    id_post = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField()
    id_autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='posts')
    id_respuestas = models.ManyToManyField('self', blank=True)
    def __str__(self) -> str:
        return self.titulo

# Modelo de Noticias
class Noticia(models.Model):
    id_noticias = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    descripcion = RichTextField()
    fecha_publicacion =  models.DateTimeField(default=timezone.now)
    imagen = ImageField(upload_to='fotonoticias', blank=True)
    categoria = models.CharField(max_length=255, blank=True)
    user = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=255, default="Noticia", choices=[('Noticia', 'Noticia'), ('Publicacion', 'Publicación')])
    def __str__(self) -> str:
        return self.titulo
# Modelo de Proyecto
class Proyecto(models.Model):
    id_pj = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    imagen = ImageField(upload_to='pjs')
    fecha_comienzo = models.DateField()
    fecha_termino = models.DateField()
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='proyectos')
    categoria = models.CharField(max_length=255)
    links = models.TextField()
    terminado = models.BooleanField()
    def __str__(self) -> str:
        return self.titulo

# Modelo de Institucion
class Institucion(models.Model):
    id_institucion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    imagen = models.BinaryField()
    link_pag_web = models.TextField()
    def __str__(self) -> str:
        return self.nombre 


# Modelo de Bolsa de Trabajo Posts
class BolsaTrabajoPost(models.Model):
    id_postbt = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_publicacion = models.DateTimeField()
    fecha_cierre = models.DateTimeField()
    id_institucion = models.ForeignKey(Institucion, on_delete=models.SET_NULL, null=True)
    id_autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='bolsa_trabajo_posts')
    def __str__(self) -> str:
        return self.titulo
# Modelo de Aplicaciones de Bolsa de Trabajo
class AplicacionBolsaTrabajo(models.Model):
    id_app = models.AutoField(primary_key=True)
    id_postbt = models.ForeignKey(BolsaTrabajoPost, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_postulacion = models.DateTimeField()
    textopos = models.TextField()
    link_cv = models.CharField(max_length=255)

class Task(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField(max_length=1000)
  created = models.DateTimeField(auto_now_add=True)
  datecompleted = models.DateTimeField(null=True, blank=True)
  important = models.BooleanField(default=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.title + ' - ' + self.user.username
  
class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    study = models.CharField(max_length=100)
    is_internal = models.BooleanField()
    image = models.ImageField(upload_to='team_members/', blank=True)

    def __str__(self):
        return self.name