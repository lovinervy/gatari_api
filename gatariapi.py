import requests
import json

url_gatari = 'https://api.gatari.pw/'


def requests_gatari(URL):
    user_information = requests.get(URL).json()
    return user_information


def user_info(user_id):
    URL = "{}users/get?u={}".format(url_gatari, user_id)
    return requests_gatari(URL)
        


def user_parser(user_id1, user_id2):
    if (user_id1 > user_id2):
        URL = "{}users/get?ids={}&ids={}".format(url_gatari, user_id2, user_id1)
    else:
        URL = "{}users/get?ids={}&ids={}".format(url_gatari, user_id1, user_id2)
    return requests_gatari(URL)


def user_modes(user_id, get_mode):
    URL = "{}user/stats?u={}&mode={}".format(url_gatari, user_id, get_mode)
    return requests_gatari(URL)


def last_plays(user_id, length):
    URL = "{}user/scores/recent?id={}&l={}".format(url_gatari, user_id, length)
    return requests_gatari(URL)
    

def recent_scores(user_id, length):
    if (length > 0) and (length <= 100):
        URL = "{}user/scores/recent?id={}&l={}".format(url_gatari, user_id, length)
    else: print("Error неверный диапазон\n")
    return requests_gatari(URL)


def best_score(user_id, length):
    URL = "{}user/scores/best?id={}&l={}".format(url_gatari, user_id, length)
    return requests_gatari(URL)    


def first_plays(user_id, length):
    URL = "{}user/scores/first?id={}&l={}".format(url_gatari, user_id, length)
    return requests_gatari(URL)


def most_plays(user_id, mode, page):
    URL = "{}user/mostplays?id={}&mode={}&page={}".format(url_gatari, user_id, \
        mode, page)
    return requests_gatari(URL)


def favorite_scores(user_id, mode, page, length):
    URL = "{}user/scores/favs?id={}&mode={}&p={}&l={}".format(url_gatari, user_id, \
        mode, page, length)
    return requests_gatari(URL)


def check_achievments(user_id, mode):
    URL = "{}user/achievements?u={}&mode={}".format(url_gatari, user_id, mode)
    return requests_gatari(URL)


def favorite_maps(user_id, page):
    URL = "{}user/favs?id={}&p={}".format(url_gatari, user_id, page)
    return requests_gatari(URL)


def pp_values(user_id):
    URL = "{}user/charts?u={}".format(url_gatari, user_id)
    return requests_gatari(URL)


def user_activity(user_id, mode):
    URL = "{}user/events?u={}&mode={}".format(url_gatari, user_id, mode)
    return requests_gatari(URL)


def score_on_map(user_id, beatmap_id):
    URL = "{}beatmap/user/score?b={}&u={}".format(url_gatari, beatmap_id, user_id)
    return requests_gatari(URL)
