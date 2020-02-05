import requests
import time
from openpyxl import load_workbook
from urllib.parse import quote

headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
}


def get_data():
    url = './config/newcoder.xlsx'
    workbook = load_workbook(url)
    sheets = workbook.get_sheet_names()
    bookSheet = workbook.get_sheet_by_name(sheets[0])

    rows = bookSheet.rows
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
        #print(who, user)

    return data


def get_contest(contest_id):
    while True:
        try:
            res = requests.get(f"https://ac.nowcoder.com/acm/contest/rank/submit-list?token=&currentContestId={contest_id}&contestList={contest_id}&_={int(time.time())}")
            break
        except Exception as e:
            print('error', str(e))
            print('try again')

    return res.text

def get_statu(val, ID) :
    try:
        qname = quote(val)
    except:
        qname = val
    url = f"https://ac.nowcoder.com/acm/contest/status-list?token=&id={ID}&searchUserName={qname}&_={int(time.time())}"
    while True:
        try:
            res = requests.get(url)
            break
        except Exception as e:
            print('error', str(e))
            print('try again')

    return res.text
