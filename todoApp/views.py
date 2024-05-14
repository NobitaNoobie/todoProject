from django.shortcuts import render
from django.http import HttpResponse

from .models import Task

# Create your views here.


#note that this view will not render the model objects. It will just render the heading 
def index(request):
    #return HttpResponse('Hello World')
    #we need to 'render' the templates here
    return render(request, 'todoApp/list.html')


def taskList(request):
    allTasks = Task.objects.all()
    context  = {"allTasks" : allTasks}
    return render(request, 'todoApp/list.html', context)
