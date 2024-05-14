from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200, primary_key=True)
    description = models.CharField(max_length=1000)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        #doing this will name the model instance in the admin panel after 'title'
        #if we do not write the str dunder method, every model object created in the admin panel will have an arbitrary confusing name
        return self.title
    
    
