from django.db import models

# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    imagem = models.ImageField(upload_to="static/images/post")
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
    # Retorna uma prévia do texto
    def previa_texto(self):
        return self.texto[:75] + '...' if len(self.texto) > 75 else self.texto