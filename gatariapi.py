import requests
import json

url_gatari = 'https://api.gatari.pw/'


def requests_gatari(URL):
    user_information = requests.get(URL).json()
    return user_information


def user_info(user_id):
    URL = f"{url_gatari}users/get?u={user_id}"
    return requests_gatari(URL)
        


def user_parser(user_id1, user_id2):
    if (user_id1 > user_id2):
        URL = f"{url_gatari}users/get?ids={user_id2}&ids={user_id1}"
    else:
        URL = f"{url_gatari}users/get?ids={user_id1}&ids={user_id2}"
    return requests_gatari(URL)


def user_modes(user_id, get_mode):
    URL = f"{url_gatari}user/stats?u={user_id}&mode={get_mode}"
    return requests_gatari(URL)


def last_plays(user_id, length):
    URL = f"{url_gatari}user/scores/recent?id={user_id}&l={length}"
    return requests_gatari(URL)
    

def recent_scores(user_id, length):
    if (length > 0) and (length <= 100):
        URL = f"{url_gatari}user/scores/recent?id={user_id}&l={length}"
    else: return "Error неверный диапазон\n"
    return requests_gatari(URL)


def best_score(user_id, length):
    URL = f"{url_gatari}user/scores/best?id={user_id}&l={length}"
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
