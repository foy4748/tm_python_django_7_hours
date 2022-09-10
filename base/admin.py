from django.contrib import admin

# Register your models here.

from .models import Room

#For including the Model in admin panel
admin.site.register(Room)
