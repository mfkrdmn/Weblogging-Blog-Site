from django.urls import path
from . import views


urlpatterns = [
    path('<slug:slug>', views.category, name="category")
]
