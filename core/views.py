from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def job_list(request):
    return render(request, 'list.html', {'title': 'Emplois & Stages'})

def formation_list(request):
    return render(request, 'list.html', {'title': 'Formations & Bourses'})

def stage_list(request):
    return render(request, 'list.html', {'title': 'Stages'})

def appel_list(request):
    return render(request, 'list.html', {'title': 'Appels d’offres & Concours'})
