from django.urls import path
from . import views


urlpatterns = [
    path('singlepage/<str:pk>', views.single_page, name="single_page"),
]
