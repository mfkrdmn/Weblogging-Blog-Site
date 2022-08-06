from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from userprofile.models import *

# Create your views here.
@login_required(login_url='/login/')
def author(request, pk):
    user_object = User.objects.get(username=pk)
    user_profile = Profile.objects.get(user=user_object)
    posted_articles = Articles.objects.filter(user=pk)

    context = {

        "posted_articles" : posted_articles,
        "user_object" : user_object,
        "user_profile" :user_profile,

    }

    return render(request, "blog.html", context)


@login_required(login_url='/login/')
def post(request):
    if request.method == "POST":

        user = request.user.username
        title = request.POST["title"]
        body = request.POST["body"]
        picture = request.FILES.get("picture")
        category = request.POST["category"]
        new_post = Articles.objects.create(user=user,title=title, picture=picture, body=body, category=category)
        new_post.save()

        return redirect('home')

    else:

        return redirect("/")

