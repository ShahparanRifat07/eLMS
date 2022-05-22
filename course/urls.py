from django.urls import path
from .views import viewAllCourse

app_name = 'course'
urlpatterns = [
    path('all_course/',viewAllCourse,name='all-course'),
]