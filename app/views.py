from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"app/index.html")

def post(request):
    return render(request,"app/post.html")

def autor(request):
    return render(request,"app/index.html")

def categoria(request):
    return render(request,"app/index.html")

def datos(request):
    return render(request,"app/index.html")