from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    bio = models.TextField(blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    def str(self):
        return f"{self.first_name} {self.last_name}"


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=50)
    license_number = models.CharField(max_length=20)
    years_of_experience = models.IntegerField()
    education = models.TextField()
    hospital = models.CharField(max_length=100)

    def str(self):
        return f"Dr. {self.user.last_name} - {self.specialty}"


class MedicalRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    record_type = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def str(self):
        return f"{self.record_type} - {self.user.username} - {self.date}"


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    reason = models.TextField()



class Medication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    schedule = models.TextField()

    def str(self):
        return f"{self.name} for {self.user.username}"


class FitnessProgram(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def str(self):
        return f"{self.name} for {self.user.username}"


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


