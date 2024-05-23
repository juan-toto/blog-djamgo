from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True, verbose_name='nombre')
    activo = models.BooleanField(default=True, verbose_name='activo')
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificacion')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre
    
class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50, unique=True, verbose_name='nombre')
    activo = models.BooleanField(default=True, verbose_name='activo')
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificacion')

    class Meta:
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Etiquetas'
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre
    
class Post(models.Model):
    titulo = models.CharField(max_length=250, verbose_name='Titulo')
    bajada = models.TextField(verbose_name='Bajada')
    contenido = models.TextField(verbose_name='Contenido')
    imagen = models.ImageField(upload_to='post', null=True, blank=True, verbose_name='imagen')
    publicado = models.BooleanField(default=False, verbose_name='Publicado')
    # Campos con relacion
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoria')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Autor')
    etiqueta = models.ManyToManyField(Etiqueta, verbose_name='Etiqueta')

    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificacion')

    class Meta:
        verbose_name = 'Publicacion'
        verbose_name_plural = 'Publicaciones'
        ordering = ['-created']

    def __str__(self):
        return self.titulo
