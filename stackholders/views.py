import profile
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Profile
from course.models import Course


# Create your views here.

def userlogin(request):
    if(request.method == "POST"):
        username = request.POST.get("user_name")
        password = request.POST.get("password")
        user = authenticate(username = username, password = password)
        print(user)
        if(user is None):
            return redirect("stackholder:login")
        else:
            if(user.is_superuser):
                login(request, user)
                return redirect("stackholder:admin-dashboard")
            elif(user.profile.isFaculty()):
                login(request, user)
                return redirect("stackholder:dashboard")
            else:
                login(request, user)
                return redirect("stackholder:dashboard")
    else:
        if (request.user.is_authenticated):
            if(request.user.is_superuser):
                return redirect("stackholder:admin-dashboard")
            elif(request.user.profile.isFaculty()):
                return redirect("stackholder:dashboard")
            else:
                return redirect("stackholder:dashboard")
        else:
            return render(request, 'stackholders/login.html')

def user_logout(request):
    logout(request)
    return redirect('stackholder:login')

def dashboard(request):
    if request.user is None:
        return redirect("stackholder:login")
    else:
        if (request.user.is_authenticated):
            user = request.user
            profile = Profile.objects.get(user = user)
            if profile.isFaculty():
                courses = Course.objects.filter(faculty = profile)
                context ={
                    'profile' : profile,
                    'courses' : courses
                }
                return render(request, 'stackholders/dashboard.html',context)
            else:
                courses = Course.objects.filter(student = profile)
                context ={
                    'profile' : profile,
                    'courses' : courses
                }
                return render(request, 'stackholders/dashboard.html',context)
        else:
            return redirect("stackholder:login")


def admin_dashboard(request):
    if(request.user.is_superuser):
        total_student = Profile.objects.filter(is_student=True).filter(is_faculty=False).count()
        total_faculty = Profile.objects.filter(is_faculty=True).count()
        total_course = Course.objects.all().count()
        
        faculties = Profile.objects.filter(is_faculty=True).order_by("-created_time")[:5]
        students = Profile.objects.filter(is_student=True).filter(is_faculty=False).order_by("-created_time")[:5]
        courses = Course.objects.all()[:10]
        context = {
            'faculties' : faculties,
            'students' : students,
            'courses' : courses,
            'total_student' : total_student,
            'total_faculty' : total_faculty,
            'total_course' : total_course
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
            
            return redirect('stackholder:admin-dashboard')
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
            dept = request.POST.get('dept')
            password = request.POST.get('password')
            user = User(username = facult_username, first_name = first_name,last_name=last_name,email=email)
            user.set_password(password)
            user.save()
            profile = Profile(user = user,is_faculty=True,is_student=False,dept = dept)
            profile.save()
            return redirect('stackholder:admin-dashboard')
        else:
            context = {
                'departments' : departments
            }
            return render(request, 'stackholders/add_faculty.html',context)
    else:
        return render(request, 'stackholders/no_access.html')



def edit_faculty(request , id):

    departments = ['CSE','EEE','BBA','CIVIL']

    if(request.user.is_superuser):
        if(request.method == "POST"):
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            dept = request.POST.get('dept')
            faculty_profile = Profile.objects.get(id = id)
            user = User.objects.get(id = faculty_profile.user.id)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.save()
            faculty_profile.dept = dept
            faculty_profile.save()
            return redirect('stackholder:admin-dashboard')
        else:
            faculty_profile = Profile.objects.get(id = id)
            context = {
                'faculty' : faculty_profile,
                'departments' : departments
            }
            return render(request, 'stackholders/edit_faculty.html',context)
    else:
        return render(request, 'stackholders/no_access.html')

def delete_faculty(request, id):
    if(request.user.is_superuser):
        faculty_profile = Profile.objects.get(id = id)
        user = User.objects.get(id = faculty_profile.user.id)
        faculty_profile.delete()
        user.delete()
        return redirect('stackholder:all-faculties')
    else:
        return render(request, 'stackholders/no_access.html')
    


def add_course(request):

    departments = ['CSE','EEE','BBA','CIVIL']
    sections = ['A','B','C','D','E','F','G','H']

    if(request.user.is_superuser):
        if(request.method == "POST"):
            title = request.POST.get('title')
            code = request.POST.get('code')
            dept = request.POST.get('dept')
            sec = request.POST.get('sec')
            course = Course(title = title,course_code = code,dept = dept,section = sec)
            course.save()
            return redirect('stackholder:admin-dashboard')
        else:
            context = {
                'departments' : departments,
                'sections' : sections,
            }
            return render(request, 'stackholders/add_course.html',context)
    else:
        return render(request, 'stackholders/no_access.html')


def assign_faculty(request ,id):

    if(request.user.is_superuser):
        if(request.method == "POST"):
            faculty_id = request.POST.get('faculty')
            faculty = User.objects.get(id = faculty_id)
            faculty_profile = Profile.objects.get(user = faculty)
            course = Course.objects.get(id = id)
            course.faculty = faculty_profile
            course.save()
            return redirect('stackholder:admin-dashboard')
        else:
            course = Course.objects.get(id = id)
            faculties = Profile.objects.filter(is_faculty = True)
            context = {
                'course' : course,
                'faculties' : faculties
            }
            return render(request, 'stackholders/assign_faculty.html',context)
    else:
        return render(request, 'stackholders/no_access.html')


def getAllStudents(request):
    students = Profile.objects.filter(is_student = True)
    context = {
        'students' : students
    }
    return render(request,'stackholders/all_students.html',context)


def getAllFaculties(request):
    faculties = Profile.objects.filter(is_faculty = True)
    context = {
        'faculties' : faculties,
    }
    return render(request,'stackholders/all_faculties.html',context)


def assign_course(request ,id):

    if(request.user.is_superuser):
        if(request.method == "POST"):

            student_profile = Profile.objects.get(id = id)
            course_id = request.POST.get('course_id')
            course = Course.objects.get(id = course_id)
            course.student.add(student_profile)
            course.save()
            return redirect('stackholder:profile', id=student_profile.user.id)
        else:
            student_profile = Profile.objects.get(id = id)
            courses = Course.objects.exclude(student = student_profile)
            context = {
                'student' : student_profile,
                'courses' : courses,
            }
            return render(request, 'stackholders/assign_course.html',context)
    else:
        return render(request, 'stackholders/no_access.html')




def profile(request,id):
    if request.user is None:
        return redirect("stackholder:login")
    else:
        user = User.objects.get(id = id)
        profile = Profile.objects.get(user = user)
        if profile.isFaculty():
            courses = Course.objects.filter(faculty = profile)
            context ={
                'profile' : profile,
                'courses' : courses
            }
            return render(request, 'stackholders/profile.html',context)
        else:
            courses = Course.objects.filter(student = profile)
            context ={
                'profile' : profile,
                'courses' : courses
            }
            return render(request, 'stackholders/profile.html',context)