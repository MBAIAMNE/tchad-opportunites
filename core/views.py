from django.shortcuts import render
from announcements.models import Annonce
def home(request):
    return render(request, 'home.html')

def job_list(request):
    annonces = Annonce.objects.filter(type='emploi')  # Change 'type' si ton champ s'appelle category
    return render(request, 'list.html', {'annonces': annonces, 'title': 'Emplois & Stages'})

def formation_list(request):
    annonces = Annonce.objects.filter(type='formation')
    return render(request, 'list.html', {'annonces': annonces, 'title': 'Formations & Bourses'})

def stage_list(request):
    annonces = Annonce.objects.filter(type='stage')
    return render(request, 'list.html', {'annonces': annonces, 'title': 'Stages'})

def appel_list(request):
    annonces = Annonce.objects.filter(type='appel')
    return render(request, 'list.html', {'annonces': annonces, 'title': 'Appels d’offres & Concours'})
