from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Patient information
class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField(verbose_name="Date of Birth")
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Visits made by patients
class Visit(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    reason = models.TextField(blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Visit for {self.patient} on {self.date.date()}"

# Diagnoses linked to visits
class Diagnosis(models.Model):
    visit = models.ForeignKey(Visit, on_delete=models.CASCADE)
    description = models.TextField()
    icd_code = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.description} ({self.icd_code})"

# Medications given to patients
class Medication(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=100, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} for {self.patient}"

# Staff profile extending default User
class StaffProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=[
        ('doctor', 'Doctor'),
        ('nurse', 'Nurse'),
        ('admin', 'Admin')
    ])

    def __str__(self):
        return f"{self.user.username} ({self.role})"
