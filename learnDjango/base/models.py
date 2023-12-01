from django.db import models

# Create your models here.

class Room(models.Model):
    #host//actual user
    #topic
    name = models.CharField(max_length=200)
    description=models.TextField(null=True,blank=True)
    #participants=
    updated = models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)
    
    #when add modal you need to make migration
    