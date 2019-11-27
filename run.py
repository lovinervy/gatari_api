import gatariapi as ga

user_id = 6246
def userinformation(user_id):
    r = ga.user_info(user_id)
    if (r["code"] == 200):
        user = r["users"][0]
        print(user)
        print("Клан: {}".format(user['abbr']))
        print("Подписчики: {}".format(user['followers_count']))
        print("id пользователя: {}".format(user['id']))
        print("Ник: {}".format(user['username']))
    elif(r["code"]== 404):
        print('User Not Found')

def last_score(user_id):
    r = ga.last_plays(user_id, 1)
    if (r["code"]== 200):
        score = r["scores"][0]
        beatmap = score["beatmap"]
        print("{}".format(score["accuracy"]))
        print("mapper: {}".format(beatmap["creator"]))
        print("song: {}".format(beatmap["song_name"]))
        print("difficulty: {}".format(beatmap["difficulty"]))
        print("link: https://osu.gatari.pw/b/{}".format(beatmap["beatmap_id"]))


def statistic(user_id):
    mods = input('asd(0-3)\n') 
    r = ga.user_modes(user_id, mods)
    print(r)
    stats = r["stats"]
    print("user id  :{}".format(stats["id"]))
    print("pp       :{}pp".format(stats["pp"]))
    print("playcount:{}".format(stats["playcount"]))
    print("avg_acc  :{}%".format(stats["avg_accuracy"]))

def recent_plays(user_id):
    r = ga.recent_scores(user_id, 5)
    print(r)


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
            print("rank:(", i["data"][1]["rank"],') ', edit_text)    
        except IndexError:
            print(edit_text)
        print('link: https://osu.gatari.pw/' + title[l+2: +r])

song_id = 1842043
def check_map(user_id, song_id):
    r = ga.score_on_map(user_id, song_id)
    score = r['score']
    x = float('{:.2f}'.format(score["accuracy"]))
    print("accuracy: {}%, rank: {}".format(x, score["rank"]))
    print(str(score["count_300"]) + '/'+ str(score["count_100"]) + '/' + str(score["count_50"]) \
        + '/' + str(score["count_miss"]))
    print('combo:', score["max_combo"])
    print('top:', score["top"])


def pp_checker(user_id):
    r = ga.pp_values(user_id)
    print('Общий рр:',r["data"][59][1])
    result1 = str(int(r["data"][59][1]) - int(r["data"][58][1]))
    result7 = str(int(r["data"][59][1]) - int(r["data"][52][1]))
    result30 = str(int(r["data"][59][1]) - int(r["data"][29][1]))
    print("За день: {} \nЗа неделю: {} \nЗа месяц: {}".format(result1, result7, result30))


#def favorite_map_check(user_id):

#recent_plays(user_id)
activity(user_id)
#check_map(user_id, song_id)
#pp_checker(user_id)
