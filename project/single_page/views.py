from multiprocessing import context
from django.shortcuts import render
from articles.models import *
from userprofile.models import *
# Create your views here.

def single_page(request, pk):

    single_post = Articles.objects.filter(id=pk)

    user_profile = Profile.objects.all()

    context ={
        "single_post" :single_post,
        "user_profile" : user_profile,
    }

    return render(request,"single_page.html", context)