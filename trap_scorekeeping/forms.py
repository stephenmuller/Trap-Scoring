
from django import forms
from .models import Post

class NewScore(forms.ModelForm):
    class Meta:
        model = Round
        fields = [
            
        ]