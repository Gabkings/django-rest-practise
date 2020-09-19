from django.contrib import admin

# Register your models here.
from .models import JobsModel

admin.site.register(JobsModel)