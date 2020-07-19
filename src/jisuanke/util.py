import requests
from hashlib import md5
import json

from openpyxl import load_workbook

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6,ru;q=0.5,zh-HK;q=0.4',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Host': 'www.jisuanke.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/84.0.4147.89 Safari/537.36 ',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin'
}

login_headers = {
    'Host': 'passport.jisuanke.com',
    'Connection': 'keep-alive',
    'Content-Length': '68',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Accept': 'application/json,text/javascript,*/*; q=0.01',
    'X-XSRF-TOKEN': 'nZjdmm5ArH1utW4PBTDLGjzhWSpWIPRQ',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64) AppleWebKit/537.36(KHTML,'
                  'likeGecko)Chrome/84.0.4147.89Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'Origin': 'https://passport.jisuanke.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://passport.jisuanke.com/?n=http%3A%2F%2Fwww.jisuanke.com%2Fcontest%2F9342%2Franklist',
    'Accept-Encoding': 'gzip,deflate,brAccept-Language:zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6,ru;q=0.5,'
                       'zh-HK;q=0.4',
    'Cookie': 'XSRF-TOKEN=nZjdmm5ArH1utW4PBTDLGjzhWSpWIPRQ; Hm_lvt_183e07aa097a1758fd6d45349e74c327=1595043550; '
              'JESONG_USER_ID=01000000012825513163509364091945; JESONG_VC=1; JESONG_AC=0; JESONG_DC=0; JESONG_IC=0; '
              'Hm_lpvt_183e07aa097a1758fd6d45349e74c327=1595165924; '
              's=eyJpdiI6IkdVdVVHVm1kMVpMZmRHRksxQTVyeGc9PSIsInZhbHVlIjoiR09CemZTczFRTlJ3T0tmaFVISG85b1Fub1BWNjVxa2EzRlE5XC9FdkcwSWJQcVJ2NzkwOHNNT3N1MEQrcTVzT0UiLCJtYWMiOiI5MDhiNmRhMTVmMjg2ZGI4MjRhODUxZDVjMzZlZTI5NDVlMTY5MTMxYzUxZmQ5NWQ0OTczMDM4MWQ3Zjg3MDQ5In0%3D '
}


def login(username, password):
    log_url = "https://passport.jisuanke.com/auth/login"
    password = password.encode("utf-8")
    username = "+86" + username
    data = {
        'account': username,
        'pwd': md5(password).hexdigest(),
        'save': 1
    }
    session = requests.session()

    while True:
        try:
            response = session.post(log_url, headers=login_headers, data=data)
            # print(response.headers)
            # print(response.status_code)
            # print(response.text)
            break
        except Exception as e:
            print('error', str(e))
            print('try again')
    return response.cookies


def get_data(contest_id, cookies):
    params = {
        'page': 1
    }
    while True:
        try:
            res = requests.get(f"https://www.jisuanke.com/contest/{contest_id}/ranklist", cookies=cookies,
                               headers=headers, allow_redirects=False, params=params)
            # print(res.headers)
            # print(res.status_code)
            # print(f"https://www.jisuanke.com/contest/{contest_id}/ranklist")
            break
        except Exception as e:
            print('error', str(e))
            print('try again')
    res = res.json()
    tot = res["last_page"]

    for i in range(2, tot + 1):
        params['page'] += 1
        response = requests.get(f"https://www.jisuanke.com/contest/{contest_id}/ranklist", cookies=cookies,
                                headers=headers, allow_redirects=False, params=params)
        next_json = response.json()
        res['data'] += next_json['data']

    return res


def get_user():
    url = './config/jisuanke.xlsx'
    workbook = load_workbook(url)
    sheets = workbook.get_sheet_names()
    book_sheet = workbook.get_sheet_by_name(sheets[0])
    rows = book_sheet.rows
    first = True
    data = {}

    for row in rows:

        if row[0].value is None:
            break
        if first:
            first = False
            continue
        who = row[0].value
        user = row[1].value
        data[who] = str(user)
        # print(who, user)

    return data
