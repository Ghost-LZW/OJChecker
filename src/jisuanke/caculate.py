

def solve(data, user):
    user_names = []
    for key, value in user.items():
        user_names.append(value)

    contest_data = {}

    p_num = 0
    rank = 0
    for person in data:
        rank += 1
        if person['name'] in user_names:
            contest_data[person['name']] = {}
            contest_data[person['name']]['solved'] = []
            contest_data[person['name']]['aSolved'] = []
            contest_data[person['name']]['totTime'] = person['cost']
            contest_data[person['name']]['attempted'] = True
            contest_data[person['name']]['rank'] = rank
            cnt = 0
            for sub_id, submit in person['cost_detail'].items():
                if submit['cost'] > 0:
                    contest_data[person['name']]['solved'].append(cnt)
                    contest_data[person['name']][cnt] = submit['submit_count']
                cnt += 1
            if p_num == 0:
                p_num = cnt

    return contest_data, p_num
