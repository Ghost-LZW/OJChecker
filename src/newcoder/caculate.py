import json
from src.newcoder import util


def solve(data, users, want=False):
    user_names = []
    for key, val in users.items():
        user_names.append(val)

    contest = json.loads(data)
    problemData = contest['data']['problemData']

    problems = {}
    for problem in problemData:
        problems[problem['problemId']] = problem['index']

    submitdata = contest['data']['submitDataList'][0]
    basicInfo = submitdata['basicInfo']
    length = (basicInfo['endTime'] - basicInfo['startTime']) // 1000

    if want:
        return {}, basicInfo['endTime']

    signUpUsers = submitdata['signUpUsers']
    user_uid = {}
    for i in signUpUsers:
        if i['name'] in user_names:
            user_uid[i['uid']] = i['name']

    #print(user)
    #print(user_new)
    contest_data = {}
    submissions = submitdata['submissions']
    #print(submission)
    for submission in submissions:
        if submission['uid'] not in user_uid:
            continue
        who = user_uid[submission['uid']]
        if who not in contest_data:
            contest_data[who] = {}
            contest_data[who]['solved'] = []
            contest_data[who]['aSolved'] = []
            contest_data[who]['totTime'] = 0
            contest_data[who]['attempted'] = False

        if submission['submitTime'] <= basicInfo['endTime']:
            contest_data[who]['attempted'] = True

        which = ord(problems[submission['problemId']]) - ord('A')

        if submission['status'] == 5 and which not in contest_data[who]['solved']:
            if submission['submitTime'] <= basicInfo['endTime']:
                contest_data[who]['solved'].append(which)
                if which not in contest_data[who]:
                    contest_data[who][which] = 0
                contest_data[who]['totTime'] += (submission['submitTime'] - basicInfo['startTime']) // 1000 + contest_data[who][which] * 20 * 60
        elif submission['status'] != 5 and which not in contest_data[who]['solved']:
            if which not in contest_data[who]:
                contest_data[who][which] = 0
            contest_data[who][which] += 1
    contest_data_f = {}
    for key, val in sorted(contest_data.items(), key=lambda item: len(item[1]['solved'])):
        contest_data_f[key] = val
    #print(contest_data_f)
    #print(contest_data['32402'])
    return contest_data_f, basicInfo['endTime']


def after_solve(data, user, ID, endTime):
    for key, val in user.items():
        print('check', key, '补题情况')
        status = json.loads(util.get_statu(val, ID))
        if val not in data:
            data[val] = {}
            data[val]['solved'] = []
            data[val]['aSolved'] = []
            data[val]['totTime'] = 0
            data[val]['attempted'] = False
        statudata = status['data']['data']
        for statu in statudata :
            which = ord(statu['index']) - ord('A')
            if statu['submitTime'] > endTime and which not in data[val]['solved'] and which not in data[val]['aSolved']:
                if statu['statusMessage'] == '答案正确':
                    data[val]['aSolved'].append(which)
                else:
                    if which not in data[val]:
                        data[val][which] = 0
                    data[val][which] += 1
