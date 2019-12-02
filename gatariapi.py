import requests
import json

url_gatari = 'https://api.gatari.pw/'


def requests_gatari(URL):
    user_information = requests.get(URL).json()
    return user_information


def user_info(u):
    URL = f"{url_gatari}users/get?u={u}"
    return requests_gatari(URL)
        

def users_info_pars(u1, u2):
    if (u1 > u2):
        URL = f"{url_gatari}users/get?ids={u2}&ids={u1}"
    else:
        URL = f"{url_gatari}users/get?ids={u1}&ids={u2}"
    return requests_gatari(URL)


def user_stats(u,mode):
    URL = f"{url_gatari}user/stats?u={u}&mode={mode}"
    return requests_gatari(URL)
    

def recent_scores(u, l, p, mode, f, ppf):
    URL = f"{url_gatari}user/scores/recent?id={u}&l={l}&p={p}&mode={mode}&f={f}&ppFilter={ppf}"
    return requests_gatari(URL)


def best_score(u, l, p, mode, mods):
    URL = f"{url_gatari}user/scores/best?id={u}&l={l}&p={p}&mode={mode}&mods={mods}"
    return requests_gatari(URL)    


def first_plays(user_id, length):
    URL = f"{url_gatari}user/scores/first?id={user_id}&l={length}"
    return requests_gatari(URL)


def most_plays(user_id, mode, page):
    URL = f"{url_gatari}user/mostplays?id={user_id}&mode={mode}&page={page}"
    return requests_gatari(URL)


def favorite_scores(user_id, mode, page, length):
    URL = f"{url_gatari}user/scores/favs?id={user_id}&mode={mode}&p={page}&l={length}"
    return requests_gatari(URL)


def check_achievments(user_id, mode):
    URL = f"{url_gatari}user/achievements?u={user_id}&mode={mode}"
    return requests_gatari(URL)


def favorite_maps(user_id, page):
    URL = f"{url_gatari}user/favs?id={user_id}&p={page}"
    return requests_gatari(URL)


def pp_values(user_id):
    URL = f"{url_gatari}user/charts?u={user_id}"
    return requests_gatari(URL)


def user_activity(user_id, mode):
    URL = f"{url_gatari}user/events?u={user_id}&mode={mode}"
    return requests_gatari(URL)


def score_on_map(user_id, beatmap_id):
    URL = f"{url_gatari}beatmap/user/score?b={beatmap_id}&u={user_id}"
    return requests_gatari(URL)
