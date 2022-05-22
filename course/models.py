
from django.db import models
from stackholders.models import Profile
from django.utils import timezone

# Create your models here.

class Course(models.Model):
    faculty = models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True,blank=True)
    title = models.CharField(max_length=128)
    course_code = models.CharField(max_length=64)
    section = models.CharField(max_length=20)
    created_time = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title


class Assignment(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    due_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Submission(models.Model):
    student = models.OneToOneField(Profile, on_delete=models.CASCADE)
    assignment = models.OneToOneField(Assignment, on_delete=models.CASCADE)
    submission_status = models.BooleanField(default=False)
    submission_time = models.DateTimeField(default=timezone.now)
    assignment_file = models.FileField(upload_to = 'uploads/')
    grade = models.IntegerField()

    def __str__(self):
        return self.student.user.first_name

class Notice(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    description = models.TextField()
    created_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
