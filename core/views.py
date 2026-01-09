from django.shortcuts import render
from announcements.models import Announcement  # Nom correct de l'app : announcements

def home(request):
    return render(request, 'home.html')

def job_list(request):
    annonces = Announcement.objects.filter(category='emploi')  # Change 'category' en ton champ réel (ex: type ou category)
    return render(request, 'list.html', {'annonces': annonces, 'title': 'Emplois & Stages'})

def formation_list(request):
    annonces = Announcement.objects.filter(category='formation')
    return render(request, 'list.html', {'annonces': annonces, 'title': 'Formations & Bourses'})

def stage_list(request):
    annonces = Announcement.objects.filter(category='stage')
    return render(request, 'list.html', {'annonces': annonces, 'title': 'Stages'})

def appel_list(request):
    annonces = Announcement.objects.filter(category='appel')
    return render(request, 'list.html', {'annonces': annonces, 'title': 'Appels d’offres & Concours'})
