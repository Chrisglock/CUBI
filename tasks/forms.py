from typing import Any
from django.forms import ModelForm
from .models import Task
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.db import models


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(label='Nombres',max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label='Apellidos',max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(RegisterUserForm,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

        
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

#class DescForm(ModelForm):
 #   class Meta:
  #      model = User
   #     fields = ['description']
#class TaskForm(ModelForm):
#    class Meta:
#        model = Task
#        fields = ['title', 'description', 'important']
#

