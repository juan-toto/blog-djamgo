from django.contrib import admin
from .models import Categoria, Etiqueta, Post, sobre_mi

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('nombre', 'activo','created')

admin.site.register(Categoria,CategoriaAdmin)

class EtiquetaAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('nombre', 'activo','created')

admin.site.register(Etiqueta,EtiquetaAdmin)

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('titulo', 'categoria','publicado', 'autor','created','post_etiqueta')
    ordering = ('autor','-created')
    search_fields = ('titulo','contenido','autor__username','categoria__nombre')
    list_filter = ('autor','categoria','etiqueta')

    def post_etiqueta(self, obj):
        return ' - '.join([t.name for t in obj.etiqueta.all().order_by('nombre')])

admin.site.register(Post,PostAdmin)

class sobreAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('descripcion','created')

admin.site.register(sobre_mi,sobreAdmin)