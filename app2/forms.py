from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    
    first_name = forms.CharField(max_length=20, label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}))
    
    last_name = forms.CharField(max_length=20, label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellido'}))
    
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}))
    
    username = forms.CharField(max_length=20, label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
    
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Contraseña'}))
    
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirmar Contraseña'}))
    
    class Meta:
        
        model=User
        
        fields=["first_name", "last_name", "email", "username", "password1", "password2"]
        
        
class Form_Login(forms.Form):
    
    username = forms.CharField(max_length=20, label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
    
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Contraseña'}))
    
    
class Form_Edit_1(forms.Form):
    
    first_name = forms.CharField(required=False, max_length=20, label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}))
    
    last_name = forms.CharField(required=False, max_length=20, label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellido'}))
    
    username = forms.CharField(required=False, max_length=20, label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
    
    email = forms.EmailField(required=False, label='', widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}))
    
    bio = forms.CharField(required=False, label='', widget = forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Bio'}))
    
    url = forms.URLField(required=False, label='', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder':'URL'}))
    
    imagen = forms.ImageField(label='Avatar',required=False)
    

class Form_Edit_2(forms.Form):
    
    password1 = forms.CharField(required=False, label='', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Nueva Contraseña'}))
    
    password2 = forms.CharField(required=False, label='', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirmar Contraseña'}))
    
    password_actual = forms.CharField(required=False, label='', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Contraseña Actual'}))
    
    
class Form_Edit_2_1(forms.Form):
    
    password1 = forms.CharField(required=False, label='', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Nueva Contraseña'}))
    
    password2 = forms.CharField(required=False, label='', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirmar Contraseña'}))
