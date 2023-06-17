from django.contrib import admin

# Register your models here.
# Register Profile model to admin site
from .models import Profile
admin.site.register(Profile)