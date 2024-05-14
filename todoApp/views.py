from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import Task
from .forms import TaskForm

# Create your views here.


#note that this view will not render anything 
def index(request):
    #return HttpResponse('Hello World')
    #we need to 'render' the templates here
    return render(request, 'todoApp/list.html')


def taskList(request):
    allTasks = Task.objects.all()
    context  = {"allTasks" : allTasks} #'allTasks' used in list.html
    return render(request, 'todoApp/list.html', context)

def taskForm(request):
    tasks = Task.objects.all() #intentionally changed the name to understand context mapping
    #note that in list.html if you remove the for loop containing the {task in tasks} part, the list won't get displayed
    #but in the taskList/ endpoint it will be displayed.
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()

    context = {"tasks": tasks, "form": form} #just pass the form in our template
    return render(request, "todoApp/list.html", context)

def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    return render(request, 'todoApp/update_task.html')
