from django.shortcuts import render

# Create your views here.

def getAllCourse(request):
    return render(request,'course.html')
