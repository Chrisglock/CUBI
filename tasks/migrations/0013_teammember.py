# Generated by Django 4.2.7 on 2023-11-07 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0012_alter_noticia_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('study', models.CharField(max_length=100)),
                ('is_internal', models.BooleanField()),
                ('image', models.ImageField(blank=True, upload_to='team_members/')),
            ],
        ),
    ]
