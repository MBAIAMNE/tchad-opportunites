from django.shortcuts import render
from announcements.models import Announcement  # Change 'announcements' si ton app s'appelle autrement (ex: core ou jobs)

def home(request):
    return render(request, 'home.html')

def job_list(request):
    annonces = Announcement.objects.filter(type='emploi')  # Adapte 'type' et 'emploi' selon ton modèle
    return render(request, 'list.html', {'annonces': annonces, 'title': 'Emplois & Stages'})

def formation_list(request):
    annonces = Announcement.objects.filter(type='formation')
    return render(request, 'list.html', {'annonces': annonces, 'title': 'Formations & Bourses'})

def stage_list(request):
    annonces = Announcement.objects.filter(type='stage')
    return render(request, 'list.html', {'annonces': annonces, 'title': 'Stages'})

def appel_list(request):
    annonces = Announcement.objects.filter(type='appel')
    return render(request, 'list.html', {'annonces': annonces, 'title': 'Appels d’offres & Concours'})
