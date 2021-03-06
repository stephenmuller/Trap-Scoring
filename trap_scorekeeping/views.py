"""trap_scorekeeping Views."""

from django.shortcuts import render, redirect
from . import logic, forms, models, settings
import math
import csv
from django.http import HttpResponse


def render_csv_request(request, user_name):
    """Returns a CSV file containing the percent values for 25 targets set up for the d3s visualization"""
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
    writer = csv.writer(response)
    write_target_data_to_csv_writer(user_name, writer)
    return response


def render_index(request):
    """renders the site index"""
    last_5 = logic.last_five_rounds()
    for round_obj in last_5:
        round_obj.score = round_obj.convert_to_int_score()
    user_list = logic.return_ten_users()
    streaks = logic.calculate_streaks()
    longest_streak = max(streaks)
    shots = logic.calculate_total_shots()
    percent_hit = math.floor(logic.hit_percentage_for_user('stephen') * 100)
    avg_score = math.floor(25 * logic.hit_percentage_for_user('stephen'))
    template_data = {
        'rounds': last_5,
        'users': user_list,
        'streaks': streaks,
        'longest_streak': longest_streak,
        'shots': shots,
        'hit_percent': percent_hit,
        'average_score': avg_score
    }
    return render(
        request,
        'trap_scorekeeping/index.html',
        template_data
    )


def render_score_entry(request, model_id=None):
    """renders the score entry page"""
    if request.method == 'POST':
        post_data = request.POST
        string_for_db = clean_query_dict_for_score_entry(post_data)
        new_round = models.Round.objects.get(id=model_id)
        new_round.score = string_for_db
        new_round.save()
        return redirect('ack_entry', model_id)
    template_data = {
        'id': model_id,
    }
    return render(request,
                  'trap_scorekeeping/score_entry.html',
                  template_data)


def render_round_entry(request):
    """renders the round entry page"""
    if request.method == 'POST':
        form = forms.NewScore(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('score_entry', model_id=instance.pk)
    else:
        form = forms.NewScore()
    template_data = {
        'form': form
    }
    return render(request,
                  'trap_scorekeeping/round_entry.html',
                  template_data)


def render_ack_entry(request, model_id=None):
    """a page for confirming round entry, deletes the new round and redirects to round_entry if the red button
    is clicked"""
    round_data = models.Round.objects.get(id=model_id)
    template_data = {
        'round_data': round_data
    }
    return render(request, 'trap_scorekeeping/ack_entry.html', template_data)


def render_round_delete(request, model_id):
    """deletes a round, redirects to round entry"""
    logic.delete_round_by_id(model_id)
    return redirect('round_entry')


def render_player_page(request, user_name):
    """renders a players page"""
    last_five = logic.last_five_rounds_for_user(user_name)
    for round_obj in last_five:
        round_obj.score = round_obj.convert_to_int_score()
    streaks = logic.calculate_streak_by_user(user_name)
    longest_streak = max(streaks)
    shots = logic.calculate_total_shots_for_user(user_name)
    percent_hit = math.floor(logic.hit_percentage_for_user(user_name) * 100)
    avg_score = math.floor(25 * logic.hit_percentage_for_user(user_name))
    user_list = logic.return_ten_users()
    template_data = {
        'last_five': last_five,
        'streaks': streaks,
        'longest_streak': longest_streak,
        'shots': shots,
        'hit_percent': percent_hit,
        'average_score': avg_score,
        'username': user_name,
        'users': user_list,
    }
    return render(request, 'trap_scorekeeping/user_page.html', template_data)


def clean_query_dict_for_score_entry(query):
    r"""Takes a query dict from the post request and sets it up for entry in the DB

    >>> data = {'t6': ['f'], 't4': ['d'], 'csrfmiddlewaretoken':
    ... ['ubFsTzaUfULAE7Eoat4Ez3tFQKd1uitwuED0ZdLCsDNpkMT4rG5NvwwSAY9xKCkY'], 't3': ['c'], 't2': ['b']}
    >>> clean_query_dict_for_score_entry(data)
    'bcdf'
    """
    t_values = ['t' + str(i) for i in range(1, 26)]
    score = [query[t_val][0] for t_val in t_values if t_val in query]
    score.sort()
    return ''.join(score)


def write_target_data_to_csv_writer(username, writer):
    """writes data to csv"""
    percents = logic.avg_score_by_target(username)
    csv_path = settings.BASE_DIR + '/trap_scorekeeping/static/trap_scorekeeping/baseaster.csv'
    with open(csv_path) as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == 'id':
                writer.writerow(row)
            else:
                key_from_csv = row[0]
                floored_percent = math.floor(percents[key_from_csv])
                row[2] = floored_percent
                writer.writerow(row)
