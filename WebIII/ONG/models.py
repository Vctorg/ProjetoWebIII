from django.db import models

# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    imagem = models.ImageField(upload_to="")
    data = models.DateTimeField(auto_now_add=True)

class Member(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    usuario = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
    admin = models.BooleanField()