from django.urls import path
from .views import getAllCourse

app_name = 'course'
urlpatterns = [
    path('',getAllCourse),
]