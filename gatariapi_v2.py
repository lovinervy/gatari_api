import requests
import json

def user_info(u):
    url_params = {'u' : u}
    r = requests.get('https://api.gatari.pw/users/get', params=url_params).json()
    return r


def user_info_pars(u1, u2):
    if (u2>u1): url_params = {'ids': [u2, u1] }
    else: url_params = { 'ids': [u1, u2] }
    r = requests.get('https://api.gatari.pw/users/get', params=url_params).json()
    return r


def user_stats(u, mode=None):
    url_params = {'u': u, 'mode' : mode}
    r = requests.get('https://api.gatari.pw/user/stats', params=url_params)
    return r


def recent_scores(u, mode, l=None, p=None, f=None, ppf=None):
    url_params = {'id': u, 'l': l, 'p': p, 'mode': mode, 'f': f, 'ppFilter': ppf}
    r = requests.get('https://api.gatari.pw/user/scores/recent', params=url_params).json()
    return r


def best_scores(u, l, p, mode, mods=None):
    url_params = {'id': u, 'l': l, 'p': p, 'mode': mode, 'mods': mods}
    r = requests.get('https://api.gatari.pw/user/scores/best', params=url_params).json()
    return r


def first_places(u, mode, p, l):
    url_params = {'id': u, 'mode': mode, 'p': p, 'l': l}
    r = requests.get('https://api.gatari.pw/user/scores/first', params=url_params).json()
    return r


def most_played(u, mode, p):
    url_params = {'id': u, 'mode': mode, 'page': p}
    r = requests.get('https://api.gatari.pw/user/mostplays', params=url_params).json()
    return r


def favorite_scores(u, mode, p, l):
    url_params = {'id': u, 'mode': mode, 'p': p, 'l': l}
    r = requests.get('https://api.gatari.pw/user/scores/favs', params=url_params).json()
    return r


def achievments(u, mode):
    url_params = {'u': u, 'mode': mode}
    r = requests.get( 'https://api.gatari.pw/user/achievements', params=url_params).json()
    return r


def favorite_maps(u, p):
    url_params = {'id': u, 'p': p}
    r = requests.get( 'https://api.gatari.pw/user/favs', params=url_params).json()
    return r


def pp_values(u, mode):
    url_params = {'u': u, 'mode': mode}
    r = requests.get('https://api.gatari.pw/user/charts', params=url_params).json()
    return r


def user_activity(u, mode):
    url_params = {'u': u, 'mode': mode}
    r = requests.get('https://api.gatari.pw/user/events', params=url_params).json()
    return r


def score_on_map(u, b, mode):
    url_params = {'b': b, 'u': u, 'mode': mode}
    r = requests.get('https://api.gatari.pw/beatmap/user/score', params=url_params).json()
    return r


def pp_leaderboard(mode, p, country=None):
    url_params = {'m': mode, 'p': p, 'country': country}
    r = requests.get('https://api.gatari.pw/leaderboard/pp', params=url_params).json()
    return r


def score_leaderboard(mode, p, country=None):
    url_params = {'m': mode, 'p': p, 'country': country}
    r = requests.get('https://api.gatari.pw/leaderboard/score', params=url_params).json()
    return r


def clans_leaderboard(p):
    url_params = {'p': p}
    r = requests.get('https://api.gatari.pw/leaderboard/clans', params=url_params).json()
    return r


def beatmap_scores(b, mode):
    url_params = {'mode': mode}
    r = requests.get(f'https://api.gatari.pw/beatmap/{b}/scores', params=url_params).json()
    return r


def beatmap_information(b):
    url_params = {'bb': b}
    r = requests.get('https://api.gatari.pw/beatmaps/get', params=url_params).json()
    return r


def pp_on_map(b, a=100, x=0, c=None, mods=0):
    url_params = {'b': b, 'a': a, 'x': x, 'c':c, 'm': mods}
    r = requests.get('https://osu.gatari.pw/api/v1/pp', params=url_params).json()
    return r


def top_scores_on_per(mode, period):
    url_params = {'mode': mode, 'period': period}
    r = requests.get('https://api.gatari.pw/top_scores', params=url_params).json()
    return r


