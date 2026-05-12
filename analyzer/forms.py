from django import forms

class ResumeUploadForm(forms.Form):

    resume = forms.FileField()

    job_description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': 6,
                'placeholder': 'Paste Job Description Here'
            }
        ),
        required=False
    )