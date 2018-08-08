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

def stories_view(request):
    if request.method == "GET":
      fetched_questions = Activity.objects.all()
    return render(request, 'templates/stories_view.html', {'question': fetched_questions})

def draw(request):
    return render(request, 'draw.html')

# # Change back later
# def stories_view(request):
#     if request.method == "GET":
#       fetched_answers = Answers.objects.all()
#     return render(request, 'templates/stories_view.html', {'answer': fetched_answers})

# Fatima's code:


# def send(request):
#     if request.method == 'POST':
#         form = SendForm(request.POST)
#         if form.is_valid():
#             send = Send.create(form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['phone'], form.cleaned_data['date'], form.cleaned_data['time'])
#             send.save()
#     else:
#         form = SendForm()
#     return render(request, 'life/send.html', {'form': form})
#
#
# def jobs(request):
#     if request.method == 'POST':
#         form = JobForm(request.POST)
#         if form.is_valid():
#             jobs = Jobs.create(form.cleaned_data['job_title'], form.cleaned_data['description'])
#             jobs.save()
#     else:
#         form = JobForm()
#     return render(request, 'life/jobs.html', {'form': form})
#
# def schedule(request):
#   if request.method == "GET":
#     all_groups = Send.objects.all()
#   return render(request, 'life/schedule.html', {'schedule_listing': all_groups})
