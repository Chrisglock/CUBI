from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import PerfilUsuario

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        perfil, _ = PerfilUsuario.objects.get_or_create(user=instance)
        perfil.nombre = instance.first_name
        perfil.email = instance.email
        perfil.save()

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.perfilusuario.save()