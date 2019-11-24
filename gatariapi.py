import requests
import json

url_gatari = 'https://api.gatari.pw/'


def requests_gatari(URL):
    user_information = requests.get(URL).json()
    print(user_information)


def user_info(user_id):
    URL = "{}users/get?u={}".format(url_gatari, user_id)
    requests_gatari(URL)   


def user_parser(user_id1, user_id2):
    if (user_id1 > user_id2):
        URL = "{}users/get?ids={}&ids={}".format(url_gatari, user_id2, user_id1)
    else:
        URL = "{}users/get?ids={}&ids={}".format(url_gatari, user_id1, user_id2)
    requests_gatari(URL)


def user_modes(user_id, get_mode):
    URL = "{}user/stats?u={}&mode={}".format(url_gatari, user_id, get_mode)
    requests_gatari(URL)


def last_plays(user_id):
    URL = "{}user/scores/recent?id={}&l=1".format(url_gatari, user_id)
    requests_gatari(URL)
    

def recent_scores(user_id, page_length):
    if (page_length > 0) and (page_length <= 100):
        URL = "{}user/scores/recent?id={}&l={}".format(url_gatari, user_id, page_length)
    else: print("Error неверный диапазон\n")
    requests_gatari(URL)


def best_score(user_id):
    URL = "{}user/scores/best?id={}&l=1".format(url_gatari, user_id)
    requests_gatari(URL)    


def first_plays(user_id):
    URL = "{}user/scores/first?id={}&l=1".format(url_gatari, user_id)
    requests_gatari(URL)


def most_plays(user_id):
    URL = "{}user/mostplays?id={}&mode=0&page=1".format(url_gatari, user_id)
    requests_gatari(URL)


def favorite_scores(user_id):
    URL = "{}user/scores/favs?id={}&mode=0&p=1&l=5".format(url_gatari, user_id)
    requests_gatari(URL)


def check_achievments(user_id):
    URL = "{}user/achievements?u={}&mode=0".format(url_gatari, user_id)
    requests_gatari(URL)


def favorite_maps(user_id):
    URL = "{}user/favs?id={}&p=1".format(url_gatari, user_id)
    requests_gatari(URL)


def pp_values(user_id):
    URL = "{}user/charts?u={}".format(url_gatari, user_id)
    requests_gatari(URL)


def user_activity(user_id):
    URL = "{}user/events?u={}&mode=0".format(url_gatari, user_id)
    requests_gatari(URL)


def score_on_map(user_id, beatmap_id):
    URL = "{}beatmap/user/score?b={}&u={}".format(url_gatari, beatmap_id, user_id)
    requests_gatari(URL)
