


import profile
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Course,Assignment,Submission,Notice
from stackholders.models import Profile
import datetime

# Create your views here.

def viewAllCourse(request):
    courses = Course.objects.all().order_by('-created_time')
    context = {
        'courses' : courses
    }
    return render(request,'all_course.html',context)

def viewDetailCourse(request,id):
    course = Course.objects.get(id = id)
    user = request.user
    if user is not None:
        profile = Profile.objects.get(user = user)
        assignments = Assignment.objects.filter(course = course)
        notices = Notice.objects.filter(course = course)
        context = {
            'profile' : profile,
            'assignments':assignments,
            'notices':notices,
            'course' : course,
        }
        return render(request, 'course.html',context)
    else:
        return redirect('stackholder:login')



def addAssignment(request, id):
    
    course = Course.objects.get(id = id)
    user = request.user

    if user is not None:
        if(request.method == "POST"):
            
            # profile = Profile.objects.get(user = user)
            title = request.POST.get("title")
            about = request.POST.get("about")
            due = request.POST.get("due")
            assignment = Assignment(course = course,title=title,description = about, due_date =due)
            assignment.save()
            return redirect("course:detail-course",id=id)
            
        else:
            context = {
                'course' : course
            }
            return render(request, 'add_assignment.html',context)
    else:
        return redirect('stackholder:login')


def addNotice(request, id):
    
    course = Course.objects.get(id = id)
    user = request.user

    if user is not None:
        if(request.method == "POST"):
            
            # profile = Profile.objects.get(user = user)
            title = request.POST.get("title")
            about = request.POST.get("about")
            notice = Notice(course = course,title=title,description = about)
            notice.save()
            return redirect("course:detail-course",id=id)
            
        else:
            context = {
                'course' : course
            }
            return render(request, 'add_notice.html',context)
    else:
        return redirect('stackholder:login')


def submission(request,course_id,assignment_id):

    course = Course.objects.get(id = course_id)
    assignment = Assignment.objects.get(id=assignment_id)

    user = request.user
    profile = Profile.objects.get(user = user)

    submission = Submission.objects.filter(assignment = assignment,student=profile)
    
    today = datetime.date.today()
    due = assignment.due_date - today
    if submission.exists():
        context = {
            'submission':submission[0],
            'course' : course,
            'assignment': assignment,
            'due':due
        }
        return render(request,'submission.html',context)
    else:
        context = {
            'submission':submission,
            'course' : course,
            'assignment': assignment,
            'due':due
        }
        return render(request,'submission.html',context)


def viewNotice(request,course_id,notice_id):
    course = Course.objects.get(id = course_id)
    notice = Notice.objects.get(id = notice_id)

    user = request.user
    if user is not None:
        context = {

            'notice': notice,
            'course' : course,
        }
        return render(request, 'notice.html',context)
    else:
        return redirect('stackholder:login')


def addSubmission(request,id):
    assignment = Assignment.objects.get(id = id)
    course_id = assignment.course.id
    user = request.user
    profile = Profile.objects.get(user =user)

    if request.method == "POST" :
        file = request.FILES["file"]
        submission = Submission(student = profile,assignment = assignment, submission_status = True,assignment_file = file)
        submission.save()
        return redirect('course:submission', course_id=course_id, assignment_id=assignment.id)

    context = {
        'assignment' : assignment,
    }
    return render(request, 'add_submission.html',context)

def search(request):
    if request.method == "POST":
        search = request.POST.get("search")
        
    return render(request,'search.html')