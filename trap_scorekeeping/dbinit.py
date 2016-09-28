"""sets up basic DB models"""

from django.db import models
from . import models, logic
from django.contrib.auth.models import User


def init_basic_defaults():
    """ensures there are defaults for the basic DB models

    >>> init_basic_defaults()
    >>> models.Shotgun.objects.all()
    <QuerySet [Shotgun('Remmington', '870 Express', '12', 26, 'none')]>
    >>> models.Shells.objects.all()
    <QuerySet [Shells('remmington', 'gameloads', '7.5', '1oz', 1290)]>
    >>> models.User.objects.all()
    <QuerySet [<User: stephen>]>
    """
    # ensures there is a user in the DB to assign rounds to
    logic.create_user('stephen', 'supersecurefakepassword')
    # sets up a shotgun, currently the rental guns at Portland Gun Club
    logic.create_new_gun_model('Remmington', '870 Express', '12', 26, 'none')
    # Sets up a basic shell model
    logic.create_new_shells_model('remmington', 'gameloads', '7.5', '1oz', 1290)
    # create a new round to satisfy the homepage stats
    logic.create_new_round(User.objects.get(username='stephen'), 'abc', '1997-07-16T19:20:30+01:00',
                           'portland gun club',
                           models.Shotgun.objects.get(), models.Shells.objects.get(), '1',
                           'no excuses!!')


def set_up_test_db():
    """sets up a DB for basic doctesting

    >>> set_up_test_db()
    >>> models.Round.objects.all()
    <QuerySet [Round(<User: test>, 'abc', datetime.datetime(1997, 7, 16, 18, 20, 30, tzinfo=<UTC>), 'portland gun club', Shotgun('beretta', 'a400', '12', 28, 'shell catcher'), Shells('remmington', 'gameloads', '7.5', '1oz', 1290), '1', 'no excuses!!'), Round(<User: test>, 'abc', datetime.datetime(1997, 7, 16, 18, 20, 30, tzinfo=<UTC>), 'portland gun club', Shotgun('beretta', 'a400', '12', 28, 'shell catcher'), Shells('remmington', 'gameloads', '7.5', '1oz', 1290), '1', 'no excuses!!'), Round(<User: test>, 'abc', datetime.datetime(1997, 7, 16, 18, 20, 30, tzinfo=<UTC>), 'portland gun club', Shotgun('beretta', 'a400', '12', 28, 'shell catcher'), Shells('remmington', 'gameloads', '7.5', '1oz', 1290), '1', 'no excuses!!'), Round(<User: test>, 'abc', datetime.datetime(1997, 7, 16, 18, 20, 30, tzinfo=<UTC>), 'portland gun club', Shotgun('beretta', 'a400', '12', 28, 'shell catcher'), Shells('remmington', 'gameloads', '7.5', '1oz', 1290), '1', 'no excuses!!'), Round(<User: test2>, 'abc', datetime.datetime(1997, 7, 16, 18, 20, 30, tzinfo=<UTC>), 'portland gun club', Shotgun('beretta', 'a400', '12', 28, 'shell catcher'), Shells('remmington', 'gameloads', '7.5', '1oz', 1290), '1', 'no excuses!!')]>
    >>> models.Shotgun.objects.all()
    <QuerySet [Shotgun('beretta', 'a400', '12', 28, 'shell catcher')]>
    >>> models.Shells.objects.all()
    <QuerySet [Shells('remmington', 'gameloads', '7.5', '1oz', 1290)]>
    >>> models.User.objects.all()
    <QuerySet [<User: test>, <User: test2>]>
    """
    logic.create_user('test', 'test', 'test')
    logic.create_user('test2', 'test2', 'test2')
    logic.create_new_gun_model('beretta', 'a400', '12', 28, 'shell catcher')
    logic.create_new_shells_model('remmington', 'gameloads', '7.5', '1oz', 1290)
    logic.create_new_round(User.objects.get(id=1), 'abc', '1997-07-16T19:20:30+01:00', 'portland gun club',
                           models.Shotgun.objects.get(id=1), models.Shells.objects.get(id=1), '1',
                           'no excuses!!')
    logic.create_new_round(User.objects.get(id=1), 'abc', '1997-07-16T19:20:30+01:00', 'portland gun club',
                           models.Shotgun.objects.get(id=1), models.Shells.objects.get(id=1), '1',
                           'no excuses!!')
    logic.create_new_round(User.objects.get(id=1), 'abc', '1997-07-16T19:20:30+01:00', 'portland gun club',
                           models.Shotgun.objects.get(id=1), models.Shells.objects.get(id=1), '1',
                           'no excuses!!')
    logic.create_new_round(User.objects.get(id=1), 'abc', '1997-07-16T19:20:30+01:00', 'portland gun club',
                           models.Shotgun.objects.get(id=1), models.Shells.objects.get(id=1), '1',
                           'no excuses!!')
    logic.create_new_round(User.objects.get(id=2), 'abc', '1997-07-16T19:20:30+01:00', 'portland gun club',
                           models.Shotgun.objects.get(id=1), models.Shells.objects.get(id=1), '1',
                           'no excuses!!')
