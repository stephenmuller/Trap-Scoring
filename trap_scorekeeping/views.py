"""trap_scorekeeping Views."""

from django.shortcuts import render
from . import logic
from . import models
from django.contrib.auth.models import User

#
# def clean_up_round_for_display(round):
#     """takes in a round object and prettyfies it
#
#     >>> logic.create_user('test', 'test', 'test')
#     >>> logic.create_new_gun_model('beretta', 'a400', '12', 28, 'shell catcher')
#     >>> logic.create_new_shells_model('remmington', 'gameloads', '7.5', '1oz', 1290)
#     >>> logic.create_new_round(User.objects.get(id=1), 24, '1997-07-16T19:20:30+01:00',
#     ... 'portland gun club', models.Shotgun.objects.get(id=1), models.Shells.objects.get(id=1), '1',
#     ... 'no excuses!!')
#     >>> models.Round.objects.all()[0]
#     Round(<User: test>, SinglesScore('a', False), datetime.datetime(1997, 7, 16, 18, 20, 30, tzinfo=<UTC>), 'portland gun club', Shotgun('beretta', 'a400', '12', 28, 'shell catcher'), Shells('remmington', 'gameloads', '7.5', '1oz', 1290), '1', 'no excuses!!')
#     """



def render_index(request):
    """renders the site index"""
    last_5 = logic.last_five_rounds()
    user_list = logic.return_ten_users()
    template_data = {
        'rounds': last_5,
        'sidebar_users': user_list
    }
    return render(
        request,
        'trap_scorekeeping/index.html',
        template_data
    )