from django.shortcuts import render, get_object_or_404
from .models import Annonce  # Ou Announcement si c’était en anglais

def home(request):
    annonces = Annonce.objects.all().order_by('-date_creation')  # Toutes les annonces sur l’accueil
    return render(request, 'home.html', {'annonces': annonces})

def annonce_detail(request, pk):
    annonce = get_object_or_404(Annonce, pk=pk)
    return render(request, 'annonce_detail.html', {'annonce': annonce})
