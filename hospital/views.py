from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def homePage(request):
	return render(request, 'hospital/home.html', {})


def addPatient(request):
	return render(request, 'hospital/add_patient.html', {})