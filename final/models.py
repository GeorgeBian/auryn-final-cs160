from django.db import models
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField


class Activity(models.Model):
    q_id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=200)
    date = models.DateField()
    active_d = models.BooleanField(default=False)
    active_q = models.BooleanField(default=False)

class Driver(models.Model):
    bio = models.CharField(max_length=1000)

class Answers(models.Model):
    q_id = models.CharField(max_length=30)
    answer = models.CharField(max_length=1000)
    timestamp = models.DateTimeField()

class Files(models.Model):
    q_id = models.CharField(max_length=30)
    file = models.FileField(upload_to='uploads/')
    timestamp = models.DateTimeField()

class Map(models.Model):
    q_id = models.CharField(max_length=30)
    lat = models.CharField(max_length=100)
    long = models.CharField(max_length=100)
    timestamp = models.DateTimeField()
