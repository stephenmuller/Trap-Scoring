
from django import forms
from .models import Round

class NewScore(forms.ModelForm):
    class Meta:
        model = Round
        fields = [
            'player', 'singles_round', 'date', 'location', 'shotgun', 'shells',
            'started_at', 'excuses'
        ]