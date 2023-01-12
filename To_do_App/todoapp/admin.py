from django.contrib import admin

# Register your models here.
from todoapp import models

admin.site.register(models.Task)