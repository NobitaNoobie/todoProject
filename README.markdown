Hi!
I will describe the project later here. 

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

I donot configure any external database for this project. I use sqlLite. 


