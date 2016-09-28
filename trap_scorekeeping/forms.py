"""Django forms setup"""
from django import forms
from .models import Round


class NewScore(forms.ModelForm):
    """form for submitting basic round details"""
    excuses = forms.CharField(required=False)
    location = forms.CharField(required=False, initial="Portland Gun Club")

    class Meta:
        """establishes the fields"""
        model = Round
        fields = [
            'player', 'location', 'shotgun', 'shells',
            'started_at', 'excuses'
        ]
        exclude = ['time', 'score']
