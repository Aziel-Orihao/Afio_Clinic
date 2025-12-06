from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Clinic System!")

from django.shortcuts import render, redirect
from .forms import PatientForm

def add_patient(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # after saving, go back to homepage
    else:
        form = PatientForm()
    return render(request, 'records/add_patient.html', {'form': form})

from .models import Patient
from django.shortcuts import render

def patient_list(request):
    patients = Patient.objects.all()  # get all patients from the database
    return render(request, 'records/patient_list.html', {'patients': patients})
