from django.shortcuts import render
from announcements.models import Announcement  # Modèle correct : Announcement

def home(request):
    return render(request, 'home.html')

def job_list(request):
    annonces = Announcement.objects.all()  # Temporaire : toutes les annonces (on filtre après)
    return render(request, 'list.html', {'annonces': annonces, 'title': 'Emplois & Stages'})

def formation_list(request):
    annonces = Announcement.objects.all()
    return render(request, 'list.html', {'annonces': annonces, 'title': 'Formations & Bourses'})

def stage_list(request):
    annonces = Announcement.objects.all()
    return render(request, 'list.html', {'annonces': annonces, 'title': 'Stages'})

def appel_list(request):
    annonces = Announcement.objects.all()
    return render(request, 'list.html', {'annonces': annonces, 'title': 'Appels d’offres & Concours'})
