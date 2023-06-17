from django.contrib import admin

# Register your models here.
# Register Transaction model to admin site
from .models import Transaction
admin.site.register(Transaction)