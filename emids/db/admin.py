from django.contrib import admin

# Register your models here.
from .models import Patient, Sex

admin.site.register(Patient)
admin.site.register(Sex)