# Generated by Django 4.2.6 on 2023-10-22 16:23

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_remove_noticia_id_autor_noticia_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='descripcion',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
