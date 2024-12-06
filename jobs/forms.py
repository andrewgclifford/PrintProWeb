from django import forms
from .models import Job, JobFile, Comment

class JobForm(forms.ModelForm):
    files = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True, 'class': 'form-control'}),
        required=False
    )
    
    class Meta:
        model = Job
        fields = [
            'title',
            'description',
            'client',
            'job_type',
            'priority',
            'deadline',
            'quantity',
            'paper_type',
            'size',
            'is_rush',
            'notes'
        ]
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'description': forms.Textarea(
                attrs={'rows': 3, 'class': 'form-control'}
            ),
            'client': forms.Select(
                attrs={'class': 'form-select'}
            ),
            'job_type': forms.Select(
                attrs={'class': 'form-select'}
            ),
            'priority': forms.Select(
                attrs={'class': 'form-select'}
            ),
            'deadline': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'},
                format='%Y-%m-%dT%H:%M'
            ),
            'quantity': forms.NumberInput(
                attrs={'class': 'form-control', 'min': '1'}
            ),
            'paper_type': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'size': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'is_rush': forms.CheckboxInput(
                attrs={'class': 'form-check-input'}
            ),
            'notes': forms.Textarea(
                attrs={'rows': 3, 'class': 'form-control'}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add placeholders
        for field in self.fields:
            if field not in ['is_rush', 'files']:
                self.fields[field].widget.attrs['placeholder'] = self.fields[field].label

        # Format initial datetime value for the deadline field
        if self.instance.pk and self.instance.deadline:
            self.initial['deadline'] = self.instance.deadline.strftime('%Y-%m-%dT%H:%M')

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
