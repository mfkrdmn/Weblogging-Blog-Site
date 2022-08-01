from multiprocessing import context
from django.shortcuts import render
from articles.models import *
# Create your views here.


def home(request):

    all_articles = Articles.objects.all()

    context = {
        "all_articles" : all_articles[:3]
    }

    return render(request, "index.html", context)
    
def contact(request):
    return render(request, "contact.html")