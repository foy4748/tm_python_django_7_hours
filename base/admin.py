from django.contrib import admin

# Register your models here.

from .models import Room,Topic,Message

#For including the Model in admin panel
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)

