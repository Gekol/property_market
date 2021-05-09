from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Property)
admin.site.register(models.Order)
admin.site.register(models.Log)
