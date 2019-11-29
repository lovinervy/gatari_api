import requests
import json
import time


def user_activity():
    URL = "https://api.gatari.pw/user/events?u=2208&mode=0"
    user_information = requests.get(URL).json()
    return user_information


time_id = None
lost_id = None


def push():
    global lost_id, time_id
    r = user_activity()
    data = r['data']
    title = data[0]['log']
    log_id = data[0]['id']
    log_check_id = data[0]['type']
    l = title.find("'/")
    r = title.find("'>")
    beatmap_id = title[l+2: +r]
    text = title[:-8+l] + title[r+2: -4]
    if (log_id != lost_id) and (log_check_id == 0):
        lost_id = log_id
        print('You', text, f'\n link: https://osu.gatari.pw/{beatmap_id}')

n = 0
while True:
    n +=1
    push()
    if(n==3):break
    time.sleep(5)