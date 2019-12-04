import requests
import json

def user_info(u):
    params = {'u' : u}
    r = requests.get('https://api.gatari.pw/users/get', params=params).json()
    print(r)


def user_stats(u, mode=None):
    url = {'u': u, 'mode' : mode}
    r = requests.get('https://api.gatari.pw/user/stats', params=url)
    print(r.url)
    print(r.json())

user_stats(u=2208)
