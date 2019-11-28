import requests
import json
import time

def user_activity():
    URL = "https://api.gatari.pw/user/events?u=2208&mode=0"
    user_information = requests.get(URL).json()
    return user_information

lost_id = None
def push():
    global lost_id
    r = user_activity()
    data = r["data"]
    title = data[0]["log"]
    l = title.find("'/")
    r = title.find("'>")
    b_id = title[l+2: +r]
    text = title[:-8+l] + title[r+2: -4]
    edit_text = text.replace('<b>', '').replace('</b>', '')
    if (b_id != lost_id):
        lost_id = b_id
        print ('You',edit_text,'\n link: https://osu.gatari.pw/' + str(b_id))

while True: 
    print(lost_id)
    push()
    time.sleep(30)