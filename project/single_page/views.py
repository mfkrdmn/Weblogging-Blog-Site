from django.shortcuts import render, redirect
from articles.models import *
from userprofile.models import *
from .models import *

# Create your views here.

def single_page(request, pk):

    single_post = Articles.objects.filter(id=pk)

    user_profile = Profile.objects.all()

    commented = Comments.objects.filter(commented_post=pk)

    commented_length = len(commented)


    if request.method == "POST":
        commenter = request.POST["commenter"]
        commented_post = pk
        comment = request.POST["comment"]
        commenter_email = request.POST["commenter_email"]
        commenterimg = request.FILES.get("image_upload")
        new_comment = Comments.objects.create(
                                                commenter=commenter, 
                                                comment=comment, 
                                                commenterimg=commenterimg, 
                                                commenter_email=commenter_email,
                                                commented_post=commented_post,
                                            )
        new_comment.save()
        
        return redirect('home')

    context = {
        "single_post" :single_post,
        "user_profile" : user_profile,
        "commented" : commented,
        "commented_length" : commented_length
    }

    return render(request,"single_page.html", context)