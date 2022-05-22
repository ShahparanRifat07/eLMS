from django.shortcuts import render
from .models import Course,Assignment,Submission,Notice

# Create your views here.

def viewAllCourse(request):
    courses = Course.objects.all().order_by('-created_time')
    context = {
        'courses' : courses
    }
    return render(request,'all_course.html',context)
