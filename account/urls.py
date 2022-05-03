import imp
from django.urls import path
from .views import home,dashboard,course,submission

urlpatterns = [
    path('',home,name="home"),
    path('dashboard/',dashboard, name = "dashboard"),
    path('course/',course, name = "course"),
    path('submission/',submission, name = "submisssion"),
]