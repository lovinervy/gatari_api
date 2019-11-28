import requests
import json
import time
#шит код, написано чтобы просто было написано
def user_activity():
    URL = "https://api.gatari.pw/user/events?u=2208&mode=0"
    user_information = requests.get(URL).json()
    return user_information
time_id = None
lost_id = None
def push():
    global lost_id, time_id
    r = user_activity()
    data = r["data"]
    title = data[0]["log"]
    l = title.find("'/")
    r = title.find("'>")
    ll = title.find("has")
    rr = title.find("place")
    text_lost = title[-1:rr] + title[ll:+20]
    b_id = title[l+2: +r]
    text = title[:-8+l] + title[r+2: -4]
    print(data[0]['id'])
    edit_text = text.replace('<b>', '').replace('</b>', '')
    if (b_id != lost_id) and (text_lost =='has lost first place') :
        lost_id = b_id
        time_id = data[0]['id']
        print ('You',edit_text,'\n link: https://osu.gatari.pw/' + str(b_id))
    elif(b_id == lost_id) and (time_id != data[0]['id']) and (text_lost =='has lost first place'):
        time_id = data[0]['id']
        print ('You',edit_text,'\n link: https://osu.gatari.pw/' + str(b_id))

def run():
    while True:
        push()
        time.sleep(60)
        print(lost_id) 
run()