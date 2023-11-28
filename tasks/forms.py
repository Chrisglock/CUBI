from typing import Any
from django.forms import ModelForm
from .models import Task,Noticia,PerfilUsuario
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms

#from tinymce import HTMLField,TinyMCE
from .models import *
class UserForm(ModelForm):
	class Meta:
		model = PerfilUsuario
		fields = '__all__'
		exclude = ['user',"alumno","admin",]

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido. Ingresa un correo electrónico válido.")
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(RegisterUserForm,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'


        
class LoginUserForm(AuthenticationForm):
    username = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Contraseña',max_length=50,widget=forms.PasswordInput(attrs={'class':'form-control'},))
    class Meta:
        model = User
        fields = ('username','password1')

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']

from django import forms
from .models import Noticia

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'descripcion', 'imagen', 'categoria', 'tipo']
    def __init__(self, *args, **kwargs):
        super(NoticiaForm, self).__init__(*args, **kwargs)
        self.fields['titulo'].widget.attrs['class'] = 'form-control'
        self.fields['categoria'].widget.attrs['class'] = 'form-control'
        self.fields['descripcion'].widget.attrs['class'] = 'form-control'
        self.fields['imagen'].widget.attrs['class'] = 'form-control'
        self.fields['tipo'].widget.attrs['class'] = 'form-control'
        self.fields['tipo'].widget = forms.HiddenInput()
        self.fields['tipo'].initial = 'Noticia'

class PubForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'categoria', 'descripcion', 'tipo']
    def __init__(self, *args, **kwargs):
        super(PubForm, self).__init__(*args, **kwargs)
        self.fields['titulo'].widget.attrs['class'] = 'form-control'
        self.fields['categoria'].widget.attrs['class'] = 'form-control'
        self.fields['descripcion'].widget.attrs['class'] = 'form-control'
        self.fields['tipo'].widget.attrs['class'] = 'form-control'
        self.fields['tipo'].widget = forms.HiddenInput()
        self.fields['tipo'].initial = 'Publicacion'

class UserForm(ModelForm):
	class Meta:
		model = PerfilUsuario
		fields = '__all__'
		exclude = ['user',"alumno","admin",]

class ContactForm(forms.Form):
    fullname = forms.CharField(label='Nombre completo', max_length=100)
    email = forms.EmailField(label='Correo electrónico')
    phone = forms.CharField(label='Número de teléfono', max_length=20)
    affair = forms.CharField(label='Asunto', max_length=100)
    message = forms.CharField(label='Mensaje', widget=forms.Textarea)      

#class DescForm(ModelForm):
 #   class Meta:
  #      model = User
   #     fields = ['description']
#class TaskForm(ModelForm):
#    class Meta:
#        model = Task
#        fields = ['title', 'description', 'important']
#

