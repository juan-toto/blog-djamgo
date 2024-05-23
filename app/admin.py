from django.contrib import admin
from .models import Categoria, Etiqueta, Post

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ['created','updated']
    list_display = ('nombre', 'activo','created')

admin.site.register(Categoria,CategoriaAdmin)

class EtiquetaAdmin(admin.ModelAdmin):
    readonly_fields = ['created','updated']
    list_display = ('nombre', 'activo','created')

admin.site.register(Etiqueta,EtiquetaAdmin)

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['created','updated']
    list_display = ('titulo', 'categoria','publicado', 'autor','created')
    ordering = ['autor','-created']
    search_fields = ['titulo']
    list_filter = ['autor']

admin.site.register(Post)
