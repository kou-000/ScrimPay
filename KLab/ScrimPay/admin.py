from django.contrib import admin

# Register your models here.
from .models import Main, User, Service, Genre

admin.site.register(Main)
admin.site.register(User)
admin.site.register(Service)
admin.site.register(Genre)