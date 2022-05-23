from django.urls import path
from .views import viewAllCourse,viewDetailCourse,addAssignment,submission,addSubmission,addNotice,viewNotice,search

app_name = 'course'
urlpatterns = [
    path('all_course/',viewAllCourse,name='all-course'),
    path('course_detail/<int:id>',viewDetailCourse,name='detail-course'),
    path('add_assignment/<int:id>',addAssignment,name='add-assignment'),
    path('add_notice/<int:id>',addNotice,name='add-notice'),
    path('add_submission/<int:id>',addSubmission,name='add-submission'),
    path('course/<int:course_id>/assinment/submission/<int:assignment_id>',submission, name = "submission"),
    path('course/<int:course_id>/notice/<int:notice_id>',viewNotice, name = "notice"),
    path('search/',search,name="search")
]