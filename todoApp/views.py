from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    #return HttpResponse('Hello World')
    #we need to 'render' the templates here
    return render(request, 'todoApp/list.html')