import requests
from bs4 import BeautifulSoup
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "coster.settings")
'''import django
django.setup()'''
# from .app.models import crawl
import random

class crawl:
    #평수
    def space(self):
        data = []
        for page in range(1, 10):
            print('page%d' % page)
            link = "https://land.naver.com/article/articleList.nhn?rletTypeCd=A01&tradeTypeCd=A1&hscpTypeCd=A01%3AA03%3AA04&cortarNo=1135010300&articleOrderCode=&siteOrderCode=&cpId=&mapX=&mapY=&mapLevel=&minPrc=&maxPrc=&minWrrnt=&maxWrrnt=&minLease=&maxLease=&minSpc=&maxSpc=&subDist=&mviDate=&hsehCnt=&rltrId=&mnex=&mHscpNo=&mPtpRange=&mnexOrder=&location=2400&ptpNo=&bssYm=&schlCd=&cmplYn=&page={0}#_content_list_target".format(page)
            req = requests.get(link)
            html = req.text
            soup = BeautifulSoup(html, 'html.parser')

            num = len(soup.select('.rate_layer > .layer > .calc_area'))
            for i in range(0, num - 1):
                items = soup.select('.rate_layer > .layer > .calc_area')[i].text.split()
                text = items[1]
                result = text[:-1]
                result.replace(" ","")
                data.append(result)

            return data

    #층수
    def floor(self):
        data = []
        for page in range(1, 10):
            link = "https://land.naver.com/article/articleList.nhn?rletTypeCd=A01&tradeTypeCd=A1&hscpTypeCd=A01%3AA03%3AA04&cortarNo=1135010300&articleOrderCode=&siteOrderCode=&cpId=&mapX=&mapY=&mapLevel=&minPrc=&maxPrc=&minWrrnt=&maxWrrnt=&minLease=&maxLease=&minSpc=&maxSpc=&subDist=&mviDate=&hsehCnt=&rltrId=&mnex=&mHscpNo=&mPtpRange=&mnexOrder=&location=2400&ptpNo=&bssYm=&schlCd=&cmplYn=&page={0}#_content_list_target".format(page)
            req = requests.get(link)
            html = req.text
            soup = BeautifulSoup(html, 'html.parser')



        num = len(soup.select('.num2 > .inner > span'))
        for i in range(0, num - 1):
            items = soup.select('.num2 > .inner > span')[i].text.split()
            text = items[0]
            if(len(text) != 3):
                result = text[:-3]
                if result == '저':
                    data.append(random.randrange(1,11))
                elif result == '중':
                    data.append(random.randrange(11,21))
                elif result == '고':
                    data.append(random.randrange(21,31))
                else:
                    data.append(result)
            else:
                result = text[0:-2]
                if result == '저':
                    data.append(random.randrange(1,11))
                elif result == '중':
                    data.append(random.randrange(11,21))
                elif result == '고':
                    data.append(random.randrange(21,31))

                else:
                    result = text[0:-2]
                    if result == '저':
                        data.append(random.randrange(1,11))
                    elif result == '중':
                        data.append(random.randrange(11,21))
                    elif result == '고':
                        data.append(random.randrange(21,31))
                    else:
                        data.append(result)
        return data


    #가격
    def price(self):
        data = []
        for page in range(1, 10):
            print('page%d' % page)
            link = "https://land.naver.com/article/articleList.nhn?rletTypeCd=A01&tradeTypeCd=A1&hscpTypeCd=A01%3AA03%3AA04&cortarNo=1135010300&articleOrderCode=&siteOrderCode=&cpId=&mapX=&mapY=&mapLevel=&minPrc=&maxPrc=&minWrrnt=&maxWrrnt=&minLease=&maxLease=&minSpc=&maxSpc=&subDist=&mviDate=&hsehCnt=&rltrId=&mnex=&mHscpNo=&mPtpRange=&mnexOrder=&location=2400&ptpNo=&bssYm=&schlCd=&cmplYn=&page={0}#_content_list_target".format(page)
            req = requests.get(link)
            html = req.text
            soup = BeautifulSoup(html, 'html.parser')

            num = len(soup.select('.num > .inner > strong'))
            for i in range(0, num - 1):
                items = soup.select('.num > .inner > strong')[i].text.split()
                text = items[0]
                result = text[:-4]
                result += '000'
                result.replace(" ","")
                data.append(result)

        return data

    def crawlRun(self):
        qubic = self.space()
        floor = self.floor()
        price = self.price()

        print('Crawling Success')

        return [qubic, floor, price]

