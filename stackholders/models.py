from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    dept = models.CharField(max_length=20)
    mobile = models.PositiveIntegerField(blank=True,null=True)
    is_student = models.BooleanField(default=True)
    is_faculty = models.BooleanField(default=False)
    city = models.CharField(max_length=64,blank=True)
    country = models.CharField(max_length=64,blank=True)
    created_time = models.DateTimeField(default=timezone.now)

    def isFaculty(self):
        if(self.is_faculty == True):
            return True
        else:
            return False

    def __str__(self):
        return self.user.username








    

