from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Job, JobFile, Comment
from .forms import JobForm, CommentForm

@login_required
def job_list(request):
    jobs = Job.objects.all().order_by('-created_at')
    
    # Filter handling
    status = request.GET.get('status')
    priority = request.GET.get('priority')
    search = request.GET.get('search')
    
    if status:
        jobs = jobs.filter(status=status)
    if priority:
        jobs = jobs.filter(priority=priority)
    if search:
        jobs = jobs.filter(title__icontains=search) | jobs.filter(job_number__icontains=search)
    
    # Pagination
    paginator = Paginator(jobs, 10)  # Show 10 jobs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'status_choices': Job.STATUS_CHOICES,
        'priority_choices': Job.PRIORITY_CHOICES,
        'current_status': status,
        'current_priority': priority,
        'search_query': search,
    }
    return render(request, 'jobs/job_list.html', context)

@login_required
def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    comments = job.comments.all().order_by('-created_at')
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.job = job
            comment.user = request.user
            comment.save()
            messages.success(request, 'Comment added successfully.')
            return redirect('job_detail', pk=pk)
    else:
        comment_form = CommentForm()
    
    context = {
        'job': job,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'jobs/job_detail.html', context)

@login_required
def job_create(request):
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            job = form.save(commit=False)
            job.created_by = request.user
            job.save()
            
            # Handle multiple file uploads
            files = request.FILES.getlist('files')
            for file in files:
                JobFile.objects.create(
                    job=job,
                    file=file,
                    uploaded_by=request.user,
                    file_type=file.content_type
                )
            
            messages.success(request, 'Job created successfully.')
            return redirect('job_detail', pk=job.pk)
    else:
        form = JobForm()
    
    return render(request, 'jobs/job_form.html', {'form': form, 'title': 'Create New Job'})

@login_required
def job_update(request, pk):
    job = get_object_or_404(Job, pk=pk)
    
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES, instance=job)
        if form.is_valid():
            job = form.save()
            
            # Handle multiple file uploads
            files = request.FILES.getlist('files')
            for file in files:
                JobFile.objects.create(
                    job=job,
                    file=file,
                    uploaded_by=request.user,
                    file_type=file.content_type
                )
            
            messages.success(request, 'Job updated successfully.')
            return redirect('job_detail', pk=job.pk)
    else:
        form = JobForm(instance=job)
    
    return render(request, 'jobs/job_form.html', {'form': form, 'title': 'Update Job'})
