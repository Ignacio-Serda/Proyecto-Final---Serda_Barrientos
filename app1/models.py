from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    
    titulo = models.CharField(max_length=100)
    subtitulo=models.CharField(max_length=300)
    cuerpo=models.TextField()
    autor=models.CharField(max_length=50)
    fecha=models.DateField(auto_now_add=True)
    imagen=models.ImageField(upload_to="blog_imgs", null=True, blank=True)
    
    
    def __str__(self):
        return f"Titulo: {self.titulo} | Subtitulo: {self.subtitulo} | Cuerpo: {self.cuerpo} | Autor: {self.autor} | Fecha: {self.fecha}"
    
class Comentario(models.Model):
    
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    
    nombre = models.CharField(max_length=100)
    
    contenido = models.CharField(max_length=300)
    
    fecha = models.DateTimeField(auto_now_add=True)