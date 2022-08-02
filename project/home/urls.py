from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('becomeablogger', views.contact, name="contact"),
]
