from django import forms
from .models import Round


class ScoreField(forms.Form):
    target_1 = forms.BooleanField(initial=True)
    target_2 = forms.BooleanField(initial=True)
    target_3 = forms.BooleanField(initial=True)
    target_4 = forms.BooleanField(initial=True)
    target_5 = forms.BooleanField(initial=True)
    target_6 = forms.BooleanField(initial=True)
    target_7 = forms.BooleanField(initial=True)
    target_8 = forms.BooleanField(initial=True)
    target_9 = forms.BooleanField(initial=True)
    target_10 = forms.BooleanField(initial=True)
    target_11 = forms.BooleanField(initial=True)
    target_12 = forms.BooleanField(initial=True)
    target_13 = forms.BooleanField(initial=True)
    target_14 = forms.BooleanField(initial=True)
    target_15 = forms.BooleanField(initial=True)
    target_16 = forms.BooleanField(initial=True)
    target_17 = forms.BooleanField(initial=True)
    target_18 = forms.BooleanField(initial=True)
    target_19 = forms.BooleanField(initial=True)
    target_20 = forms.BooleanField(initial=True)
    target_21 = forms.BooleanField(initial=True)
    target_22 = forms.BooleanField(initial=True)
    target_23 = forms.BooleanField(initial=True)
    target_24 = forms.BooleanField(initial=True)
    target_25 = forms.BooleanField(initial=True)

class NewScore(forms.ModelForm):
    class Meta:
        model = Round
        fields = [
            'player', 'location', 'shotgun', 'shells',
            'started_at', 'excuses'
        ]
        exclude = ['time', 'score']
