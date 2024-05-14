#create model forms here
from django import forms

from .models import Task

class TaskForm(forms.ModelForm):
    class Meta: 
        model = Task
        fields = "__all__"
        exclude = ["created"] #it is a non editable field, we cannot create a form field out of this. It will throw an error. That's why we exclude this
