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

def questionview(request):
    return render(request, 'questionview.html')

def qanda(request):
    if request.method == "GET":
    	fetched_questions = Activity.objects.all()
    return render(request, 'qanda.html', {'question': fetched_questions}) 

def savedrideranswer(request):
	if request.method == "GET":
		fetched_questions = QA.objects.all()
	return render(request, 'stories_view.html', {'savedrideranswer': fetched_questions})


#def savedrawing(request):


#def savedmap(request):

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

def activities(request):
    if request.method == "GET":
    	fetched_questions = Activity.objects.all()
    return render(request, 'activities.html', {'question': fetched_questions})

def bio(request):
	if request.method == 'POST':
		form = DriverForm(request.POST)
		if form.is_valid():
			send = Driver.create(form.cleaned_data['bio'])
			print("here")
			send.save()
	else:
		form = DriverForm()
	return render(request, 'bio.html', {'driverbio':form})

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
<<<<<<< HEAD


def sent_add_activity(request):
    if request.method == "GET":
      fetched_questions = Activity.objects.all()
    return render(request, 'acitivites.html', {'question': fetched_questions})

=======
>>>>>>> 917b4d39aff50d7c0de4259e94937d4d0a0def9b

def stories_view(request):
    if request.method == "GET":
      fetched_questions = Activity.objects.all()
<<<<<<< HEAD
    return render(request, 'stories_view.html', {'question': fetched_questions})
=======
      maps = Map_Q.objects.all()
    return render(request, 'stories_view.html', {'question': fetched_questions, 'map':maps})
>>>>>>> 917b4d39aff50d7c0de4259e94937d4d0a0def9b

def change_activity(request):
    if request.method == "GET":
      fetched_questions = Activity.objects.all()
    return render(request, 'change_activity.html', {'question': fetched_questions})
<<<<<<< HEAD

def change_bio(request):
    if request.method == "GET":
      fetched_questions = Driver.objects.all()
    return render(request, 'change_bio.html', {'bio': fetched_questions})

def printfordriver(request):
	if request.method == "GET":
		fetched_questions = Activity.objects.all()
	return render(request, 'change_activity.html', {'question': fetched_questions})
=======
>>>>>>> 917b4d39aff50d7c0de4259e94937d4d0a0def9b

def draw(request):
    return render(request, 'draw.html')

<<<<<<< HEAD
=======
def driverview(request):
    return render(request, 'driverview.html')

def activities(request): 
    return render(request, 'activities.html')
>>>>>>> 917b4d39aff50d7c0de4259e94937d4d0a0def9b
