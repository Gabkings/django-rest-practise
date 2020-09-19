from django.contrib import admin

from news.models import NewsModel, Journalist

# Register your models here.

admin.site.register(NewsModel)
admin.site.register(Journalist)
