from django.contrib import admin
from .models import Job, JobFile, Comment

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('job_number', 'title', 'client', 'status', 'priority', 'deadline')
    list_filter = ('status', 'priority', 'job_type')
    search_fields = ('job_number', 'title', 'description')
    date_hierarchy = 'created_at'

@admin.register(JobFile)
class JobFileAdmin(admin.ModelAdmin):
    list_display = ('job', 'file_type', 'uploaded_by', 'uploaded_at')
    list_filter = ('file_type', 'uploaded_at')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('job', 'user', 'created_at')
    list_filter = ('created_at',) 