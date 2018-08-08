from django import forms
from django.core.exceptions import ValidationError
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField

class ActivityEditForm(forms.Form):
  question = forms.CharField(max_length=200)

class RiderAnswerForm(forms.Form):
  answer = forms.CharField(label = "Type Here:", max_length = 1000)

# def __init__(self, *args, **kwargs):
#     super(ActivityEditForm, self).__init__(*args, **kwargs)
#     self.fields['date'].widget.attrs['class'] = 'datetimepicker'
