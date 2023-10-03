from django.contrib import admin
from .models import Task,Usuario, Post, Noticia, Proyecto, Institucion, BolsaTrabajoPost, AplicacionBolsaTrabajo

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
  readonly_fields = ('created', )

admin.site.register(Task, TaskAdmin)

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    pass

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    pass

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    pass

@admin.register(Institucion)
class InstitucionAdmin(admin.ModelAdmin):
    pass

@admin.register(BolsaTrabajoPost)
class BolsaTrabajoPostAdmin(admin.ModelAdmin):
    pass

@admin.register(AplicacionBolsaTrabajo)
class AplicacionBolsaTrabajoAdmin(admin.ModelAdmin):
    pass
