import profile
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Profile


# Create your views here.

def userlogin(request):
    if(request.method == "POST"):
        username = request.POST.get("user_name")
        password = request.POST.get("password")
        user = authenticate(username = username, password = password)
        print(user)
        if(user is None):
            return redirect("login")
        else:
            if(user.is_superuser):
                login(request, user)
                return redirect("admin-dashboard")
            elif(user.profile.isFaculty()):
                login(request, user)
                return redirect("dashboard")
            else:
                login(request, user)
                return redirect("dashboard")
    else:
        if (request.user.is_authenticated):
            if(request.user.is_superuser):
                return redirect("admin-dashboard")
            elif(request.user.profile.isFaculty()):
                return redirect("dashboard")
            else:
                return redirect("dashboard")
        else:
            return render(request, 'stackholders/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def dashboard(request):
    return render(request, 'stackholders/dashboard.html')

def admin_dashboard(request):
    if(request.user.is_superuser):
        total_student = Profile.objects.filter(is_student=True).filter(is_faculty=False).count()
        total_faculty = Profile.objects.filter(is_faculty=True).count()
        
        faculties = Profile.objects.filter(is_faculty=True).order_by("-created_time")[:5]
        students = Profile.objects.filter(is_student=True).filter(is_faculty=False).order_by("-created_time")[:5]
        context = {
            'faculties' : faculties,
            'students' : students,
            'total_student' : total_student,
            'total_faculty' : total_faculty,
        }
        return render(request, 'stackholders/admin_dashboard.html',context)
    else:
        return render(request, 'stackholders/no_access.html')

def add_student(request):

    departments = ['CSE','EEE','BBA','CIVIL']

    if(request.user.is_superuser):
        if(request.method == "POST"):
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            dept = request.POST.get('dept')
            student_id = request.POST['id']
            password = request.POST['password']
            user = User(username = student_id, first_name = first_name,last_name=last_name,email=email)
            user.set_password(password)
            user.save()
            profile = Profile(user = user,dept = dept)
            profile.save()
            
            return redirect('admin-dashboard')
        else:
            context = {
                'departments' : departments
            }
            return render(request, 'stackholders/add_student.html',context)
    else:
        return render(request, 'stackholders/no_access.html')

def add_faculty(request):

    departments = ['CSE','EEE','BBA','CIVIL']

    if(request.user.is_superuser):
        if(request.method == "POST"):
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            facult_username = request.POST.get('faculty_username')
            password = request.POST.get('password')
            user = User(username = facult_username, first_name = first_name,last_name=last_name,email=email)
            user.set_password(password)
            user.save()
            profile = Profile(user = user,is_faculty=True,is_student=False)
            profile.save()
            return redirect('admin-dashboard')
        else:
            context = {
                'departments' : departments
            }
            return render(request, 'stackholders/add_faculty.html',context)
    else:
        return render(request, 'stackholders/no_access.html')
    
