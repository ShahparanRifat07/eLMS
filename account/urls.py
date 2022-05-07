import imp
from django.urls import path
from .views import home,dashboard,course,submission,notice,courseSearch,userProfile

urlpatterns = [
    path('',home,name="home"),
    path('dashboard/',dashboard, name = "dashboard"),
    path('course/<int:id>',course, name = "course"),
    path('course/<int:course_id>/assinment/submission/<int:assignment_id>',submission, name = "submission"),
    path('course/<int:course_id>/notice/<int:notice_id>',notice, name ="notice"),
    path('course/search/',courseSearch,name="search"),
    path('user/profile/',userProfile,name="profile"),
]