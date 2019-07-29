from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Movie(models.Model):
    poster = models.ImageField(upload_to = "static/images/poster", null=True, blank=True)
    titulo = models.CharField(max_length=256, unique=True)
    genero = models.CharField(max_length=256)
    sinopse = models.TextField(blank=True)
    ano = models.IntegerField()
    trailer = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.titulo

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username
