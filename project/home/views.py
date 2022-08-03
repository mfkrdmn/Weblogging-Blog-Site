from django.shortcuts import render, redirect
from articles.models import *
from .models import *
from single_page.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login/')
def home(request):

    lastly_addeds = Articles.objects.all().order_by("-date_posted")

    all_articles = Articles.objects.all()

    all_comments = Comments.objects.all()   

    commented = Comments.objects.all()
    
    commented_length = len(commented)

    #commented_post a eriştiğin an iş biter

    context = {
        "lastly_addeds" : lastly_addeds[:3],
        "all_articles" : all_articles,
        "all_comments" : all_comments[:5],
        "commented" :commented,
        "commented_length" :commented_length,
    }

    return render(request, "index.html", context)

    
def contact(request):

    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        reason = request.POST["reason"]
        

        newblogger = New_Blogger.objects.create(name=name, email=email, reason=reason)
        newblogger.save()
        messages.info(request, 'Your request has been sent')

    return render(request, "contact.html")

