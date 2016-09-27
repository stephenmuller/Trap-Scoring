from django import forms
from .models import Round


class NewScore(forms.ModelForm):
    excuses = forms.CharField(required=False)
    location = forms.CharField(required=False, initial="Portland Gun Club")

    class Meta:
        model = Round
        fields = [
            'player', 'location', 'shotgun', 'shells',
            'started_at', 'excuses'
        ]
        exclude = ['time', 'score']
