from django.urls import path
from .views import (admin_dashboard,
                    add_student,
                    add_faculty,
                    userlogin,
                    dashboard,
                    user_logout,
                    add_course)

app_name ='stackholder'
urlpatterns = [
    path('',userlogin,name="login"),
    path('admin_dashboard/',admin_dashboard,name="admin-dashboard"),
    path('add_student/',add_student,name="add-student"),
    path('add_faculty/',add_faculty,name="add-faculty"),
    path('dashboard/',dashboard,name="dashboard"),
    path('add_course/',add_course,name="add-course"),
    path('logout',user_logout,name="logout"),
]