from .models import sobre_mi, Categoria

def ctx_dic_sobre(request):
    ctx_sobre = {}
    ctx_sobre['SOBRE'] = sobre_mi.objects.latest("created")
    return ctx_sobre

def ctx_dic_categoria(request):
    ctx_categoria = {}
    ctx_categoria['categoria'] = Categoria.objects.filter(activo=True)

    return ctx_categoria