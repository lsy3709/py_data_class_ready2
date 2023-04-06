import time
import bs4
import urllib.request
import ssl
import pymysql
from tkinter import *
from tkinter import messagebox

ssl_context = ssl.SSLContext()
ssl_context.verify_mode = ssl.CERT_NONE
imgLinkUrl = ""

## 함수 선언 부분
def insertData() :
    con, cur = None, None
    data1, data2, data3, data4 = "", "", "", ""
    sql=""

    con = pymysql.connect(host='127.0.0.1', user='root', password='1234', database='naverDB', charset='utf8')
    cur = con.cursor()

    data1 = edt1.get(); data2 = edt2.get(); data3 = edt3.get(); data4 = edt4.get()
    try :
        sql = "INSERT INTO userTable VALUES('" + data1 + "','" + data2 + "','" + data3 + "'," + data4 + ")"
        cur.execute(sql)
    except :
        messagebox.showerror('오류', '데이터 입력 오류가 발생함')
    else :
        messagebox.showinfo('성공', '데이터 입력 성공')
    con.commit()
    con.close()

nateUrl = "https://news.nate.com/recent?mid=n0100"
while True :
    htmlObject = urllib.request.urlopen(nateUrl,context=ssl_context)
    webPage = htmlObject.read()
    bsObject = bs4.BeautifulSoup(webPage, 'html.parser')
    tag_list = bsObject.findAll('div', {'class': 'mlt01'})

    print('###### 실시간 뉴스 속보 #######')
    num = 1
    for tag in tag_list :

        subject = tag.find('strong', {'class': 'tit'}).text
        link = tag.find('a', {'class': 'lt1'})['href']
        imgLink = tag.find('em',{'class':'mediatype'})
        if imgLink != None:
            imgLinkUrl = imgLink.find('img')['src']
        else :
            imgLinkUrl = '이미지가 존재 하지 않음'
        pressAndDate = tag.find('span', {'class': 'medium'}).text
        pressAndDate.replace('\t',' ')
        pressAndDate.replace('\n', '')

        if len(pressAndDate.split()) == 3 :
            press, pDate, pTime = pressAndDate.split()
        elif len(pressAndDate.split()) == 4 :
            press1,press2, pDate, pTime = pressAndDate.split()
            press = press1+press2
        else :
            continue

        print('(' , num, ')', subject)
        print('\t https:'+link, press, pDate, pTime)
        print('\t imgLink : https:'+ imgLinkUrl)
        num += 1

    time.sleep(60)