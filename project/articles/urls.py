from django.urls import path
from . import views


urlpatterns = [

    path('myblog/<str:pk>/', views.myblog, name="myblog"),
    path('post', views.post, name="post"),

]
