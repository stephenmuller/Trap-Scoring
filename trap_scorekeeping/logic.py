"""trap_scorekeeping Logic."""

from django.db import migrations, models
from . import models
from django.db.models import Q


def last_five_rounds():
    """querys for the last five rounds and returns a list"""
    return Round.objects.all()[::-1][:5]