from django import forms
from app1.models import *

class Form_Blog(forms.Form):
    
    titulo = forms.CharField(max_length=100, label='', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Título'}))
    
    subtitulo = forms.CharField(max_length=300, label='', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Subtítulo'}))
    
    cuerpo = forms.CharField(label='', widget = forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Texto'}))
    
    autor = forms.CharField(label='', max_length=50, widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Autor'}))
    
    imagen = forms.ImageField()
    
class Edit_Form_Blog(forms.Form):
    
    titulo = forms.CharField(label='', max_length=100, widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Título'}))
    
    subtitulo = forms.CharField(label='', max_length=300,  widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Subtítulo'}))
    
    cuerpo = forms.CharField(label='', widget = forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Texto'}))
    
class Form_Comentario(forms.Form):
    
    nombre = forms.CharField(label='', max_length=100, widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Nombre'}))
    
    contenido = forms.CharField(label='', widget = forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Texto'}))
