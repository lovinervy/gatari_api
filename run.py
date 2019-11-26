import gatariapi as ga

user_id = 1015
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
    print(r)


#recent_plays(user_id)
userinformation(user_id)