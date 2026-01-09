from django.shortcuts import render
from announcements.models import *  # Import tout pour éviter l'erreur

def home(request):
    return render(request, 'home.html')

def job_list(request):
    annonces = Annonce.objects.all()  # Affiche tout pour l’instant
    return render(request, 'list.html', {'annonces': annonces, 'title': 'Emplois & Stages'})

def formation_list(request):
    annonces = Annonce.objects.all()
    return render(request, 'list.html', {'annonces': annonces, 'title': 'Formations & Bourses'})

def stage_list(request):
    annonces = Annonce.objects.all()
    return render(request, 'list.html', {'annonces': annonces, 'title': 'Stages'})

def appel_list(request):
    annonces = Annonce.objects.all()
    return render(request, 'list.html', {'annonces': annonces, 'title': 'Appels d’offres & Concours'})
