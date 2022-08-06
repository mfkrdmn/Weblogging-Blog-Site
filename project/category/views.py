from django.shortcuts import render
from articles.models import *
# Create your views here.

def category(request, slug):

    single_post = Articles.objects.filter(category__name=slug)

    slug = Category.objects.filter(slug=slug)

    context = {
        "single_post" :single_post,
        "slug" :slug,
    }


    return render(request, "category.html", context)
