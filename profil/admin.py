from django.contrib import admin
from .models import MyProject, GuestBook

admin.site.register(MyProject)
admin.site.register(GuestBook)