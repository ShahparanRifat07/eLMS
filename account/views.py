from multiprocessing import context
from django.shortcuts import render

# Create your views here.
course_list = [
    {
        'id': 1,
        'title': "Web Programming",
        'dept': "CSE",
        'course_code': "Spring 221 CSE 4165/CSE 465 ",
        'notice' : [
            {'id': 1, 'title': "Notice1"},
            {'id': 2, 'title': "Notice2"},
            {'id': 3, 'title': "Notice3"},
        ],
        'assignment' : [
            {'id': 1, 'title': "Assignment1"},
            {'id': 2, 'title': "Assignment2"},
            {'id': 3, 'title': "Assignment3"},
        ],
    },
    {
        'id': 2,
        'title': "System Analysis and Design",
        'dept': "CSE",
        'course_code': "Spring 221 CSE 3411/CSI 311",
        'notice' : [
            {'id': 1, 'title': "Notice1"},
        ],
        'assignment' : [
            {'id': 1, 'title': "Assignment1"},
            {'id': 2, 'title': "Assignment2"},
        ],
    },
    {
        'id': 3,
        'title': "Operating Systems",
        'dept': "CSE",
        'course_code': "Spring 221 CSE 4509/CSI 309",
        'notice' : [
            {'id': 1, 'title': "Notice1"},
            {'id': 2, 'title': "Notice2"},
        ],
        'assignment' : [
            {'id': 1, 'title': "Assignment1"},
        ],
    }
]

def home(request):
    return render(request, 'login.html')


def dashboard(request):
    context = {
        'course_list' : course_list,
    }
    return render(request, 'dashboard.html', context)


def course(request,id):
    course = course_list[id-1]
    context ={
        "course" : course,
    }
    return render(request, 'course.html',context)


def submission(request,course_id,assignment_id):
    course = course_list[course_id-1]
    assignment = course['assignment'][assignment_id-1]

    context ={
        "course" : course,
        "assignment" : assignment,
    }
    return render(request, 'submission.html',context)


def notice(request,course_id,notice_id):
    course = course_list[course_id-1]
    notice = course['notice'][notice_id-1]
    context ={
        "course" : course,
        "notice" : notice,
    }
    return render(request,'notice.html',context)

def courseSearch(request):
    return render(request,'search.html')

def userProfile(request):
    return render(request,'profile.html')
