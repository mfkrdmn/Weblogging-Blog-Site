from django.shortcuts import render, redirect
from articles.models import *
from .models import *
from single_page.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@login_required(login_url='/login/')
def home(request):

    lastly_addeds = Articles.objects.all().order_by("-date_posted")

    all_articles = Articles.objects.all()

    all_comments = Comments.objects.all()   

    commented = Comments.objects.all()

    # a = Articles.objects.values("title")  ile models dan sağlanan verinin tekine ulaşılabilir

    #Pagination

    contact_list = Articles.objects.all()
    paginator = Paginator(contact_list, 5) # Show 5 articles per page

    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles = paginator.page(paginator.num_pages)

    commented_length = len(commented)

    context = {
        "lastly_addeds" : lastly_addeds[:3],
        "all_articles" : all_articles,
        "all_comments" : all_comments[:5],
        "commented" :commented,
        "commented_length" :commented_length,
        "articles" : articles,
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

