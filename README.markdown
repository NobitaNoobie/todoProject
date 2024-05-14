Hi!
This repo is maintained and authored by Tiyasa Khan. This project is a django CRUD app example. I will dynamically maintain notes and important topics I have used to develop this app, in the current file. I have taken reference from several online resources, including Django official documentation, Stack overflow, and you tube, to enhance my way of perception to write these notes. The templates will serve as a reference for my future self. I will also add boilerplate code to be re-used. 

STEPS:-----------------------------------------------------

Let's get on describing the project setup:
1. the project is made inside the django-env virtual environment and make the app.
    cd django-env
    Scripts\activate
    cd..
    django-admin startproject todoProject
    cd todoProject
    py manage.py startapp todoApp

2. make a superuser and start the django admin 
    py manage.py createsuperuser
    py manage.py runserver
now navigate to the port where the development server is active, and navigate to /admin/ to access the admin panel

I do not configure any external database for this project. I use sqlLite. 

3. make models/edit models in the models.py file. after completing editing/creating models do the following:
    py manage.py makemigrations
    py manage.py migrate


4. IF YOU HAVE MADE CHANGES TO YOUR MODEL, then you can view the same in the 'admin' panel by visiting the '/admin' endpoint. But, IF YOU ARE MAKING A MODEL FOR THE FIRST TIME, for being able to view it in the panel, we need to register your newly created model. Follow these steps to register a NEW model EVERY TIME YOU MAKE ONE:
    Step 1: Go to appName/admin.py
    Step 2: from .models import ModelName
    or, from .models import * #to import all models in that file
    Step 3: admin.site.register(ModelName1)
            admin.site.register(ModelName2)
    Step 4: visit /admin to view changes and add model instances

5. Add objects to your database in the Django admin panel.

6. Now we can render these Model objects using a template. We do this rendering to the frontend part in views.py file.
def taskList(request):
    allTasks = Task.objects.all()
    context  = {"allTasks" : allTasks} #Context dictionary
    return render(request, 'todoApp/list.html', context)

7. Next go to the list.html file to edit the template.

8. To make it more interactive so that the user can actually mimic the add/delete/edit of tasks that is happening in the admin panel, we need to create a form. Now instead of writing redundant code, we can directly map the Model structure to make a form. In this way we will not have to make an HTML, then take additional efforts to map the model fields in the HTML. 
This is done using ModelForm

9. To map the Model into frontend template, we use ModelForm. We can select what fields will be shown. This will allow the user to directly add Todo "Tasks" from the frontend, without having to manually access the Django admin. All changes made will be reflected in the Django admin as well.
Follow these steps to make model form an render to frontend:
    1. in our app directory make a file called __models.py__
    2. 

    

DEFINITIONS:-----------------------------------------------

1. HttpResponse v/s Render:
HttpResponse returns an Http Response object while the Render will return an HTML page. 

render is basically a wrapper around a HttpResponse which renders a template. It will take a template name as an argument, and then render this template with the given parameters and return an HttpResponse object.


2. Context dictionary:

3. Model form: 





