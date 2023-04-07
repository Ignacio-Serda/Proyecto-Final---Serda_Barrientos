from django.db import models
from django.contrib.auth.models import User


class Avatar(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.imagen}"
    
class Bio_Url(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    bio = models.CharField(max_length=300)
    
    url = models.URLField()