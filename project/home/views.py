from django.shortcuts import render, redirect
from articles.models import *
from .models import *
from single_page.models import *
# Create your views here.


def home(request):

    all_articles = Articles.objects.all()

    all_comments = Comments.objects.all()
    

    #commented_post a eriştiğin an iş biter

    context = {
        "all_articles" : all_articles[:3],
        "all_comments" : all_comments[:5],
    }

    return render(request, "index.html", context)

    
def contact(request):

    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        reason = request.POST["reason"]

        newblogger = New_Blogger.objects.create(name=name, email=email, reason=reason)
        newblogger.save()


    return render(request, "contact.html")