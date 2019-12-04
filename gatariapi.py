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


def first_places(u, l, mode, p):
    URL = f"{url_gatari}user/scores/first?id={u}&mode={mode}&p={p}&l={l}"
    return requests_gatari(URL)


def most_played(u, mode, p):
    URL = f"{url_gatari}user/mostplays?id={u}&mode={mode}&page={p}"
    return requests_gatari(URL)


def favorite_scores(u, mode, p, l):
    URL = f"{url_gatari}user/scores/favs?id={u}&mode={mode}&p={p}&l={l}"
    return requests_gatari(URL)


def check_achievments(u, mode):
    URL = f"{url_gatari}user/achievements?u={u}&mode={mode}"
    return requests_gatari(URL)


def favorite_maps(u, p):
    URL = f"{url_gatari}user/favs?id={u}&p={p}"
    return requests_gatari(URL)


def pp_values(u, mode):
    URL = f"{url_gatari}user/charts?u={u}&mode={mode}"
    return requests_gatari(URL)


def user_activity(u, mode):
    URL = f"{url_gatari}user/events?u={u}&mode={mode}"
    return requests_gatari(URL)


def score_on_map(u, b, mode):
    URL = f"{url_gatari}beatmap/user/score?b={b}&u={u}&mode={mode}"
    return requests_gatari(URL)


def pp_leaderboard(mode, p, country):
    URL = f"{url_gatari}leaderboard/pp?m={mode}&p={p}&country={country}"
    return requests_gatari(URL)


def score_leaderboard(mode, p, country):
    URL = f"{url_gatari}leaderboard/score?m={mode}&p={p}&country={country}"
    return requests_gatari(URL)


def clans_leaderboard(p):
    URL = f"{url_gatari}leaderboard/clans?p={p}"
    return requests_gatari(URL)


def beatmap_scores(b, mode):
    URL = f"{url_gatari}beatmap/{b}/scores?mode={mode}"
    return requests_gatari(URL)


def beatmap_information(b):
    URL = f"{url_gatari}beatmaps/get?bb={b}"
    return requests_gatari(URL)


def pp_on_map(b, a, x, c, mods):
    URL = f"https://osu.gatari.pw/api/v1/pp?b={b}&a={a}&x={x}&c={c}&m={mods}"
    return requests_gatari(URL)


def top_scores_on_period(mode, period):
    URL = f"{url_gatari}top_scores?mode={mode}&period={period}"
    return requests_gatari(URL)