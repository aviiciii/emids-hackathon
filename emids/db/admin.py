from django.contrib import admin

# Register your models here.
from .models import Patient, Sex, Bloodgroup, Doctor, Appointment, Examination, Medicine, User

admin.site.register(User)
admin.site.register(Patient)
admin.site.register(Sex)
admin.site.register(Bloodgroup)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Examination)
admin.site.register(Medicine)