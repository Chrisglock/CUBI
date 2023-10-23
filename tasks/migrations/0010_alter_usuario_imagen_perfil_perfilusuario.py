# Generated by Django 4.2.5 on 2023-10-23 16:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0009_alter_noticia_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='imagen_perfil',
            field=models.ImageField(blank=True, default='profile.png', null=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='PerfilUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('descripcion', models.TextField(null=True)),
                ('Linkedin', models.URLField(blank=True, null=True)),
                ('alumno', models.BooleanField(default=False, null=True)),
                ('imagen_perfil', models.ImageField(default='profile.png', null=True, upload_to='')),
                ('admin', models.BooleanField(default=False, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
