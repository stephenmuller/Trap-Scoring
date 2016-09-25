from django import forms
from .models import Round


class NewScore(forms.ModelForm):
    excuses = forms.CharField(required=False)
    class Meta:
        model = Round
        fields = [
            'player', 'location', 'shotgun', 'shells',
            'started_at', 'excuses'
        ]
        exclude = ['time', 'score']
