from django.contrib import admin

# Register your models here.
# configuration file for the built-in Admin app
from .models import Student

admin.site.register(Student)