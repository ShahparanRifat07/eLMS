from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'login.html')

def dashboard(request):
    return render(request,'dashboard.html')

def course(request):
    return render(request,'course.html')

def submission(request):
    return render(request,'submission.html')