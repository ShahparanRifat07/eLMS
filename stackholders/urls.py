from django.urls import path
from .views import (admin_dashboard,
                    add_student,
                    add_faculty,
                    userlogin,
                    dashboard,
                    user_logout,
                    add_course,
                    assign_faculty,
                    getAllStudents,
                    assign_course,
                    assign_course_to_student)

app_name ='stackholder'
urlpatterns = [
    path('',userlogin,name="login"),
    path('admin_dashboard/',admin_dashboard,name="admin-dashboard"),
    path('add_student/',add_student,name="add-student"),
    path('add_faculty/',add_faculty,name="add-faculty"),
    path('dashboard/',dashboard,name="dashboard"),
    path('add_course/',add_course,name="add-course"),
    path('assign_faculty/<int:id>',assign_faculty,name="assign-faculty"),
    path('assign_course/<int:id>',assign_course,name="assign-course"),
    path('assign_course/<int:course_id>/student/<int:student_id>',assign_course,name="assign-course-student"),
    path('all_students',getAllStudents,name="all-students"),
    path('logout',user_logout,name="logout"),
]