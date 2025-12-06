from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Patient, Visit, Diagnosis, Medication, StaffProfile

admin.site.register(Patient)
admin.site.register(Visit)
admin.site.register(Diagnosis)
admin.site.register(Medication)
admin.site.register(StaffProfile)
