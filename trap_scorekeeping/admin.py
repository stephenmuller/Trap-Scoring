"""trap_scorekeeping Admin Configuration."""

from django.contrib import admin
from . import models

admin.site.register(models.Shotgun)
admin.site.register(models.Shells)
admin.site.register(models.SinglesScore)
admin.site.register(models.Round)
