from ast import Sub
from django.contrib import admin
from .models import Course,Assignment,Notice,Submission
# Register your models here.


admin.site.register(Course)
admin.site.register(Assignment)
admin.site.register(Notice)
admin.site.register(Submission)