from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Job(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('prepress', 'Pre-press'),
        ('printing', 'Printing'),
        ('finishing', 'Finishing'),
        ('delivered', 'Delivered'),
        ('completed', 'Completed')
    ]
    
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('urgent', 'Urgent')
    ]

    JOB_TYPES = [
        ('digital', 'Digital Printing'),
        ('offset', 'Offset Printing'),
        ('large_format', 'Large Format'),
        ('vinyl', 'Vinyl/Cutting'),
        ('other', 'Other')
    ]

    job_number = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    client = models.ForeignKey('accounts.Client', on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='medium')
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    job_type = models.CharField(max_length=20, choices=JOB_TYPES, default='digital')
    quantity = models.IntegerField(default=1)
    paper_type = models.CharField(max_length=100, blank=True)
    size = models.CharField(max_length=50, blank=True)
    finishing_options = models.JSONField(default=dict)
    cost_estimate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_rush = models.BooleanField(default=False)
    notes = models.TextField(blank=True)
    proof_approved = models.BooleanField(default=False)
    proof_approved_at = models.DateTimeField(null=True, blank=True)
    proof_approved_by = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name='approved_jobs'
    )

    def __str__(self):
        return f"{self.job_number} - {self.title}"

class JobFile(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='job_files/')
    file_type = models.CharField(max_length=50)
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) 