from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def rider2(request):
	return render(request, 'rider2.html')

def rider1(request):
	return render(request, 'rider1.html')

def edit_activities(request):
	return render(request, 'edit_activities.html')

def stories_view(request):
	return render(request, 'stories_view.html')
