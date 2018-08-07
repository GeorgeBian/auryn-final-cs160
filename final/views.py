from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def rider2(request):
	return render(request, 'rider2.html')
