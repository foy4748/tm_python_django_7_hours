from django.db import models

# Create your models here.

class Room(models.Model):
    #host
    #topic
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    #participants 

    # auto_now updates each time we save/update the row
    updated = models.DateTimeField(auto_now=True)

    # auto_now_add updates for first time we save the row
    # auto_now updates each time we save/update the row
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
