from django.contrib import admin
from .models import *

admin.site.register(UserProfile)
admin.site.register(Doctor)
admin.site.register(MedicalRecord)
admin.site.register(Appointment)
admin.site.register(Medication)
admin.site.register(FitnessProgram)
admin.site.register(Notification)
