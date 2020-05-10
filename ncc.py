from src.newcoder import util, caculate
from src import checker

print('contest id:')
ID = input()
# ID = 3002
user = util.get_data()
# print(user)

print('''
input the Index
    1.赛事信息(包括rank)及补题信息
    2.赛事信息及补题信息
    3.仅获取补题信息
''')

opt = int(input())
# opt = 1
json = util.get_contest(ID)

if opt == 1:
    data, endTime = caculate.solve(json, user)
    caculate.solve_rank(data, user, ID)
elif opt == 2:
    data, endTime = caculate.solve(json, user)
else:
    data, endTime = caculate.solve(json, user, True)

# print(data)
# print(data['32402'])

caculate.after_solve(data, user, ID, endTime)

print('题目数量')
totNum = int(input())
# totNum = 10
print(data)
result = checker.check(data, totNum, './config/newcoder.xlsx', opt == 1)
cnt = 0
while True:
    try:
        result.save("result" + str(cnt) + ".xlsx")
        break
    except Exception as e:
        print('error ', str(e))
        print('try again')
        cnt += 1
