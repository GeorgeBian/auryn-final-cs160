from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')
def rider1(request):
    return render(request, 'rider1.html')
def activity(request):
    return render(request, 'edit_activities.html')
def story_view(request):
    return render(request, 'stories_view.html')
def draw(request):
    return render(request, 'draw.html')
