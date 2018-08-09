from django import forms
from django.core.exceptions import ValidationError
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField

class ActivityEditForm(forms.Form):
  question = forms.CharField(label = "Add your question here: ", max_length=200)

class RiderAnswerForm(forms.Form):
  answer = forms.CharField(label = "Type Here:", max_length = 1000)

class QAEditForm(forms.Form):
  youranswer = forms.CharField(label = "Your Answer Here:", max_length = 3000)

class DriverForm(forms.Form):
  bio = forms.CharField(label="Edit Your Bio Here:", max_length = 1000)