from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth import authenticate, login
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from final.models import *
from .forms import *
import datetime

def index(request):
    return render(request, 'index.html')

def map(request):
	now = datetime.datetime.now()
	if request.method == 'POST':
		if 'coord' in request.POST:
			coord = request.POST['coord'].split(',')
			lat = coord[0]
			lon = coord[1]
			pin = Map_Q.create(lat, lon, now)
			pin.save()
			# print(Map_Q.objects.all())
	return render(request, 'question_map.html')

def rider2(request):
	return render(request, 'rider2.html')

def rider1(request):
	return render(request, 'rider1.html')

def edit_activities(request):
    now = datetime.datetime.now()
    if request.method == 'POST':
        form = ActivityEditForm(request.POST)
        if form.is_valid():
            send = Activity.create(form.cleaned_data['question'], now)
            send.save()
    else:
        form = ActivityEditForm()
    return render(request, 'edit_activities.html', {'form':form})

def add_activity(request):
    now = datetime.datetime.now()
    if request.method == 'POST':
        form = ActivityEditForm(request.POST)
        if form.is_valid():
            send = Activity.create(form.cleaned_data['question'], now)
            send.save()
    else:
        form = ActivityEditForm()
    return render(request, 'add_activity.html', {'form':form})

def stories_view(request):
    if request.method == "GET":
      fetched_questions = Activity.objects.all()
    return render(request, 'stories_view.html', {'question': fetched_questions})

def change_activity(request):
    if request.method == "GET":
      fetched_questions = Activity.objects.all()
    return render(request, 'templates/change_activity.html', {'question': fetched_questions})

def draw(request):
    return render(request, 'draw.html')

def driverview(request):
    return render(request, 'driverview.html')

def activities(request): 
    return render(request, 'activities.html')
