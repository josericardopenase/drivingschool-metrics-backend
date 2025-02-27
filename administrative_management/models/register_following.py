from django.db import models

from administrative_management.models import Student, Registration
from business.models import Section
from human_resources.models import Administrative


class FollowingPlan(models.Model):
    is_active = models.BooleanField(default=True)

class FollowingSchedule(models.Model):
    name = models.CharField(max_length=100)
    following = models.ForeignKey(FollowingPlan, on_delete=models.CASCADE)
    task_type = models.ForeignKey('administrative_management.FollowingForm', on_delete=models.CASCADE)
    loop = models.BooleanField(default=True)
    days_since_register = models.IntegerField(default=0)
    repeat_every_days = models.IntegerField(default=0)

class FollowingForm(models.Model):
    type = models.CharField(max_length=120)
    name = models.CharField(max_length=100)
    description = models.TextField()

class Following(models.Model):
    register =  models.ForeignKey(Registration, on_delete=models.CASCADE)
    following_plan = models.ForeignKey(FollowingPlan, on_delete=models.CASCADE)


class FollowingTask(models.Model):
    following = models.ForeignKey(Following, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    form = models.ForeignKey(FollowingForm, on_delete=models.CASCADE)

class FollowingLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    registration = models.ForeignKey(Registration, on_delete=models.CASCADE)
    done_by = models.ForeignKey(Administrative, on_delete=models.CASCADE)