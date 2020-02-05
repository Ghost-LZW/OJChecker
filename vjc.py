from src.vjudge import caculate, util
from src import checker

print("login username: ")
username = input()
print("login password: ")
password = input()

cookies = util.login(username, password)

contest = []
print("比赛序号 正赛")
t = input()
contest.append(t)

print("比赛序号 重现赛")
t = input()
contest.append(t)

data = []
for cont in contest:
    json = util.get_contest(cont, cookies)
    data.append(caculate.solve(json))

for key, val in data[1].items():
    if key not in data[0]:
        data[0][key] = {}
        data[0][key]['solved'] = []
        data[0][key]['aSolved'] = []
        data[0][key]['totTime'] = 0
        data[0][key]['attempted'] = False
    for k, v in val.items():
        if k == 'solved':
            if len(v) > 0:
                data[0][key]['solved'] = v
        elif k == 'aSolved':
            data[0][key]['aSolved'] = list(set(data[0][key]['aSolved'] + v))
        elif k == 'totTime':
            if v > 0:
                data[0][key]['totTime'] = v
        elif k == 'attempted':
            if v:
                data[0][key]['attempted'] = True
        else:
            if k in data[0][key]:
                data[0][key][k] += v
            else:
                data[0][key][k] = v

print('题目数量')
totNum = int(input())
#totNum = 13
result = checker.check(data[0], totNum, './config/vjudge.xlsx')
cnt = 0
while True:
    try:
        result.save("result" + str(cnt) + ".xlsx")
        break
    except:
        cnt += 1

