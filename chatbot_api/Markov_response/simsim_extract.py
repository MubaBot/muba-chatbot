# -*- coding: utf-8 -*-'
import requests



headers={'Host':'www.simsimi.com','Accept':'application/json, text/javascript, */*; q=0.01','X-Requested-With':'XMLHttpRequest'}

headers['User-Agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
headers['Content-Type']= 'application/json; charset=utf-8'
headers['Referer']= 'http://www.simsimi.com/AppCopyMain'
headers['Accept-Encoding']= 'gzip, deflate'
headers['Accept-Language']= 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'


cookies={}
cookies['dotcom_session_key']='s%3AGHqbM-3Sm9X7ctb2XTIe4-q7fmhVVy1L.PBovB25GrzUvxdXnwi5korcPUZ%2FdcgIDtpjYKZ%2BT20g'
# cookies['_ga']='GA1.2.1063788982.1535069766'
# cookies['_gid']='GA1.2.2000200833.1535069766'
# cookies['user_displayName']='%EA%B9%80%EC%84%B8%ED%9D%AC'
# cookies['user_photo']='undefined'
cookies['lc']='ko'
# cookies['lname']='%ED%95%9C%EA%B5%AD%EC%96%B4'; 494668b4c0ef4d25bda4e75c27de2817=22e12afe-3ad0-4b00-933c-e2e0c70a5fb9%3A3%3A2; normalProb=7; currentChatCnt=0; bbl_cnt=9

import json,time

x='안녕'
x_b=''
ff=open('req_res.txt','a+')
with open('res.txt','a+') as f:
    # for i in range(10000):
    while(1):
        time.sleep(0.5)
        URL='http://www.simsimi.com/getRealtimeReq?lc=ko&ft=1&normalProb=7&reqText={}&status=W&talkCnt=0'.format(x)
        res=requests.get(URL,headers=headers,cookies=cookies)
        print(res)
        xx=json.loads(res.text)['respSentence']
        print(xx,x)
        if(x==xx or x_b==xx):
            x='뭐해'
            x_b=''
        else:
            x_b=x
            x=xx
        f.write(x+'\n')
        ff.write(x_b+' : '+x+'\n')
ff.close()