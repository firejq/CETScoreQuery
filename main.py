# -*- coding: UTF-8 -*-
# Author： firejq
# Created on 2017/8/23
import requests
import json
import sys
from bs4 import BeautifulSoup


def query(name, id_card, jb):
    zkz_url = 'http://app.cet.edu.cn:7066/baas/app/setuser.do?method=UserVerify'
    zkz_postdata = {
        'action': '',
        'params': json.dumps({
            "ks_xm": name,
            "ks_sfz": id_card,
            "jb": jb
        })
    }
    zkz_query = requests.post(url=zkz_url, data=zkz_postdata)
    zkz = json.loads(zkz_query.content)['ks_bh']

    score_url = 'http://www.chsi.com.cn/cet/query'
    score_getdata = {
        'zkzh': zkz,
        'xm': name
    }
    score_query_headers = {
        'Referer': 'http://www.chsi.com.cn/cet/',
        'Cookie': 'JSESSIONID=585FDCDE6A256DF086B6320056528E38; aliyungf_tc=AQAAAODGXH0+uwMA/SHfDvzrwCJnctoY; acw_tc=AQAAAHkk0kv4ygMA/SHfDt/AnSyLDeqq'
    }
    score_query = requests.get(
        url=score_url,
        params=score_getdata,
        headers=score_query_headers)

    bs = BeautifulSoup(score_query.text, 'lxml')
    score = bs.select('.colorRed')[0]
    print('准考证号：' + zkz)
    print('姓名：' + name)
    print('成绩：' + score.text.strip())


name = sys.argv[1]
id_card = sys.argv[2]
if sys.argv[3] == '4':
    jb = 1
elif sys.argv[3] == '6':
    jb = 2
query(name, id_card, jb)
