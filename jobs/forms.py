from django import forms
from .models import Job, JobFile, Comment

class JobForm(forms.ModelForm):
    files = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}),
        required=False
    )
    
    class Meta:
        model = Job
        fields = [
            'job_number',
            'title',
            'description',
            'client',
            'job_type',
            'priority',
            'due_date',
            'quantity',
            'paper_size',
            'paper_type',
            'special_instructions'
        ]
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3}),
            'special_instructions': forms.Textarea(attrs={'rows': 3}),
            'job_type': forms.Select(attrs={'class': 'form-select'}),
            'priority': forms.Select(attrs={'class': 'form-select'}),
            'client': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap classes to all form fields
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
            if field != 'files':  # Don't add placeholder to file input
                self.fields[field].widget.attrs.update({
                    'placeholder': self.fields[field].label
                })

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 2,
                'class': 'form-control',
                'placeholder': 'Add a comment...'
            })
        }
