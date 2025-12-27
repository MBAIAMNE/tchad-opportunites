from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Job, Opportunity

def job_list(request):
    jobs = Job.objects.all().order_by('-created_at')
    return render(request, 'announcements/job_list.html', {'jobs': jobs})

def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    return render(request, 'announcements/job_detail.html', {'job': job})

def opportunity_list(request):
    opportunities = Opportunity.objects.all().order_by('-created_at')
    return render(request, 'announcements/opportunity_list.html', {'opportunities': opportunities})

def opportunity_detail(request, pk):
    opportunity = get_object_or_404(Opportunity, pk=pk)
    return render(request, 'announcements/opportunity_detail.html', {'opportunity': opportunity})

@login_required
def apply_job(request, pk):
    job = get_object_or_404(Job, pk=pk)
    messages.success(request, f'Vous avez postulé à l\'offre "{job.title}" ! Nous transmettrons votre candidature.')
    # Plus tard on pourra enregistrer la candidature dans une table
    return redirect('job_detail', pk=pk)