# """trap_scorekeeping Logic."""
#
# from django.db import migrations, models
# from .models import Round
# from django.db.models import Q
#
#
# def last_five_rounds():
#     """querys for the last five rounds and returns a list"""
#     return Round.objects.all()[::-1][:5]
#
# # def metrics_for_round_details(user, metric):
# #     """plz test me"""
# #     return Round.objects.filter(name=user, metric)
#
# def generate_filter():
#     """
#
#     >>> generate_filters('')
#
#     """