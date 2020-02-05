import json


def solve(data):
    contest = json.loads(data)

    length = contest['length'] // 1000

    user = contest['participants']
    user_new = {}
    for key, val in user.items():
        user_new[val[0]] = key
    #print(user)
    #print(user_new)
    contest_data = {}
    submission = contest['submissions']
    #print(submission)
    for val in submission:
        val[0] = str(val[0])
        if user[val[0]][0] not in contest_data:
            contest_data[user[val[0]][0]] = {}
            contest_data[user[val[0]][0]]['solved'] = []
            contest_data[user[val[0]][0]]['aSolved'] = []
            contest_data[user[val[0]][0]]['totTime'] = 0
            contest_data[user[val[0]][0]]['attempted'] = False

        if val[3] <= length:
            contest_data[user[val[0]][0]]['attempted'] = True

        if val[2] == 1 and val[1] not in contest_data[user[val[0]][0]]['solved'] and val[1] not in contest_data[user[val[0]][0]]['aSolved']:
            if val[3] <= length:
                contest_data[user[val[0]][0]]['solved'].append(val[1])
                if val[1] not in contest_data[user[val[0]][0]]:
                    contest_data[user[val[0]][0]][val[1]] = 0
                contest_data[user[val[0]][0]]['totTime'] += val[3] + contest_data[user[val[0]][0]][val[1]] * 20 * 60
            else:
                contest_data[user[val[0]][0]]['aSolved'].append(val[1])

        elif val[2] == 0 and val[1] not in contest_data[user[val[0]][0]]['solved'] and val[1] not in contest_data[user[val[0]][0]]['aSolved']:
            if val[1] not in contest_data[user[val[0]][0]]:
                contest_data[user[val[0]][0]][val[1]] = 0
            contest_data[user[val[0]][0]][val[1]] += 1
    contest_data_f = {}
    for key, val in sorted(contest_data.items(), key=lambda item: len(item[1]['solved'])):
        contest_data_f[key] = val
    #print(contest_data_f)
    #print(contest_data['The__Flash'])
    return contest_data_f

