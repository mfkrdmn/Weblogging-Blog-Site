from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def register(request):
    return render(request, "register.html")

def login(request):
    return render(request, "login.html")

def blog(request):
    return render(request, "blog.html")

def contact(request):
    return render(request, "contact.html")