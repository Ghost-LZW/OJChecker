from src.jisuanke import caculate, util
from src import checker
from getpass import getpass
import json

username = input("input JSK username: ")  # "18580619816"
password = getpass("input JSK password: ")

cookie = util.login(username, password)

ID = input("contest ID: ")  # 9342

user = util.get_user()

# print(user)

# jsk = open("jsk.json")
data = util.get_data(ID, cookie)  # json.load(jsk)

data, problem_num = caculate.solve(data['data'], user)

# print(data)

result = checker.check(data, problem_num, './config/jisuanke.xlsx', True, "jsk")

# with open("./jsk.json", "w") as jsk:
#    jsk.write(json.dumps(data))
cnt = 0
while True:
    try:
        result.save("jskResult" + str(cnt) + ".xlsx")
        break
    except Exception as e:
        print('error ', str(e))
        print('try again')
        cnt += 1

