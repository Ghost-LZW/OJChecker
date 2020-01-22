import requests

headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
}


def login(username, password):
    logUrl = "https://vjudge.net/user/login"
    data = {
        'username': username,
        'password': password
    }
    seesion = requests.session()
    response = seesion.post(logUrl, headers=headers, data=data)
    return response.cookies


def get_contest(contest_id, cookies):
    res = requests.get(f"https://vjudge.net/contest/rank/single/{contest_id}", cookies=cookies)
    return res.text
