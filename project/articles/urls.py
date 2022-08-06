from django.urls import path
from . import views


urlpatterns = [

    path('author/<str:pk>/', views.author, name="author"),
    path('post', views.post, name="post"),

]
