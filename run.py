import gatariapi as ga

user_id = 2056
def userinformation(user_id):
    r = ga.user_info(user_id)
    if (r["code"] == 200):
        user = r["users"][0]
        print(f"Клан: {user['abbr']}")
        print(f"Подписчики: {user['followers_count']}")
        print(f"id пользователя: {user['id']}")
        print(f"Ник: {user['username']}")
    elif(r["code"]== 404):
        print('User Not Found')

def last_score(user_id):
    r = ga.last_plays(user_id, 1)
    if (r["code"]== 200):
        score = r["scores"][0]
        beatmap = score["beatmap"]
        print(f'{score["accuracy"]:.2f}%\nmapper: {beatmap["creator"]}\nsong: {beatmap["song_name"]}'
        f'difficulty: {beatmap["difficulty"]}\nlink: https://osu.gatari.pw/b/{beatmap["beatmap_id"]}')


def statistic(user_id):
    mods = 0 
    r = ga.user_modes(user_id, mods)
    stats = r["stats"]
    print(f'user id  :{stats["id"]}\npp       :{stats["pp"]}pp\n'
    f'playcount:{stats["playcount"]}\navg_acc  :{stats["avg_accuracy"]:.2f}%')

def recent_plays(user_id):
    r = ga.recent_scores(user_id, 1)
    scores = r["scores"]
    for i in scores:
        print(i['beatmap']['song_name'])
        print(f"rank: {i['ranking']}, accuracy: {i['accuracy']:.2f}, combo: {i['max_combo']}/{i['beatmap']['fc']}")
        print(str(i['pp'])+'pp')


def activity(user_id):
    r = ga.user_activity(user_id, 0)
    data = r["data"]
    for i in data:
        title = i["log"]
        l = title.find("'/")
        r = title.find("'>")
        text = title[:-8+l] + title[r+2: -4]
        edit_text = text.replace('<b>', '').replace('</b>', '')
        try:
            print(f'rank:({i["data"][1]["rank"]})', edit_text)    
        except IndexError:
            print(edit_text)
        print('link: https://osu.gatari.pw/' + title[l+2: +r])

song_id = 1842043
def check_map(user_id, song_id):
    r = ga.score_on_map(user_id, song_id)
    score = r["score"]    
    if(score != None):
        x = float(f'{score["accuracy"]:.2f}')
        print(f'accuracy: {x}%, rank: {score["rank"]}')
        print(f'{score["count_300"]}/{score["count_100"]}/{score["count_50"]}/{score["count_miss"]}')
        print('combo:', score["max_combo"])
        print('top:', score["top"])
    else:
        print('User in this map not found')
    

def pp_checker(user_id):
    r = ga.pp_values(user_id)
    result1 = str(int(r["data"][59][1]) - int(r["data"][58][1]))
    result7 = str(int(r["data"][59][1]) - int(r["data"][52][1]))
    result30 = str(int(r["data"][59][1]) - int(r["data"][29][1]))
    print('Общий рр:',r["data"][59][1])
    print(f'За день: {result1} \nЗа неделю: {result7} \nЗа месяц: {result30}')


def favorite_map_check(user_id):
    page = 5
    r = ga.favorite_maps(user_id, page)
    print(r)


favorite_map_check(user_id)
'''import time
time.sleep(5)
print('userinformation')
userinformation(user_id)
time.sleep(5)
print('\n\nrecent_play')
recent_plays(user_id)
time.sleep(5) 
print('\n\nactivity')
activity(user_id)
time.sleep(5)
print('\n\ncheck_map')
check_map(user_id, song_id)
time.sleep(5)
print('\n\npp_checker')
pp_checker(user_id)
time.sleep(5)
print('\n\nlast_score')
last_score(user_id)
time.sleep(5)
print('\n\nstatistic')
statistic(user_id)
'''
