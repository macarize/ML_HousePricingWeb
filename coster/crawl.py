import requests
from bs4 import BeautifulSoup
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "coster.settings")
import django
django.setup()
# from .app.models import crawl

#평수
def space():
    req = requests.get('https://land.naver.com/article/articleList.nhn?rletTypeCd=A01&tradeTypeCd=A1&hscpTypeCd=A01%3AA03%3AA04&cortarNo=1135010300&articleOrderCode=&siteOrderCode=&cpId=&mapX=&mapY=&mapLevel=&minPrc=&maxPrc=&minWrrnt=&maxWrrnt=&minLease=&maxLease=&minSpc=&maxSpc=&subDist=&mviDate=&hsehCnt=&rltrId=&mnex=&mHscpNo=&mPtpRange=&mnexOrder=&location=2400&ptpNo=&bssYm=&schlCd=&cmplYn=&page=1#_content_list_target')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    data = []
    num = len(soup.select('.rate_layer > .layer > .calc_area'))
    for i in range(0, num - 1):
        items = soup.select('.rate_layer > .layer > .calc_area')[i].text.split()
        text = items[1]
        result = text[:-1]
        data.append(result)

    return data

#층수
def floor():
    req = requests.get('https://land.naver.com/article/articleList.nhn?rletTypeCd=A01&tradeTypeCd=A1&hscpTypeCd=A01%3AA03%3AA04&cortarNo=1135010300&articleOrderCode=&siteOrderCode=&cpId=&mapX=&mapY=&mapLevel=&minPrc=&maxPrc=&minWrrnt=&maxWrrnt=&minLease=&maxLease=&minSpc=&maxSpc=&subDist=&mviDate=&hsehCnt=&rltrId=&mnex=&mHscpNo=&mPtpRange=&mnexOrder=&location=2400&ptpNo=&bssYm=&schlCd=&cmplYn=&page=1#_content_list_target')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    data = []
    num = len(soup.select('.num2 > .inner > span'))
    for i in range(0, num - 1):
        items = soup.select('.num2 > .inner > span')[i].text.split()
        text = items[0]
        result = text[:-3]
        data.append(result)

    return data

#가격
def price():
    req = requests.get('https://land.naver.com/article/articleList.nhn?rletTypeCd=A01&tradeTypeCd=A1&hscpTypeCd=A01%3AA03%3AA04&cortarNo=1135010300&articleOrderCode=&siteOrderCode=&cpId=&mapX=&mapY=&mapLevel=&minPrc=&maxPrc=&minWrrnt=&maxWrrnt=&minLease=&maxLease=&minSpc=&maxSpc=&subDist=&mviDate=&hsehCnt=&rltrId=&mnex=&mHscpNo=&mPtpRange=&mnexOrder=&location=2400&ptpNo=&bssYm=&schlCd=&cmplYn=&page=1#_content_list_target')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    data = []
    num = len(soup.select('.num > .inner > strong'))
    for i in range(0, num - 1):
        items = soup.select('.num > .inner > strong')[i].text.split()
        text = items[0]
        result = text[:-4]
        result += '000'
        data.append(result)

    return data

if __name__ == '__main__':
    data1 = space()
    print(data1)
    data2 = floor()
    print(data2)
    data3 = price()
    print(data3)