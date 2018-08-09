"""final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('map/', views.map, name='map'),
    path('rider2/', views.rider2, name='rider2'),
    path('stories_view/', views.stories_view, name='stories_view'),
<<<<<<< HEAD
    path('activities/', views.activities, name='activities'),
=======
    path('edit_activities/', views.edit_activities, name='edit_activities'),

>>>>>>> 917b4d39aff50d7c0de4259e94937d4d0a0def9b
    path('change_activity/', views.change_activity, name='change_activity'),
    path('add_activity/', views.add_activity, name='add_activity'),
    path('rider1/',views.rider1, name='rider1'),
    path('draw/',views.draw, name='draw'),
<<<<<<< HEAD
    path('questionview/', views.questionview, name='questionview'),
    path('qanda/', views.qanda, name='qanda'),
    path('activities/', views.activities, name='activities'),
    path('change_bio/', views.change_bio, name='change_bio'),
    path('bio/', views.bio, name='bio')

=======

    path('activities/', views.activities, name='activities'),
    path('driverview/', views.driverview, name='driverview'),
>>>>>>> 917b4d39aff50d7c0de4259e94937d4d0a0def9b
]
