from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from jobs.models import Job

@login_required
def dashboard(request):
    context = {
        'active_jobs_count': Job.objects.filter(status='active').count(),
        'completed_jobs_count': Job.objects.filter(status='completed').count(),
        'pending_jobs_count': Job.objects.filter(status='pending').count(),
        'recent_jobs': Job.objects.order_by('-created_at')[:5],
    }
    return render(request, 'dashboard.html', context)

def index(request):
    if request.user.is_authenticated:
        return dashboard(request)
    return render(request, 'index.html')
