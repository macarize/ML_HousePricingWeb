import os
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import random


class testCrawl:
    # mk 부동산 test
    BASE = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(BASE, "etc\chromedriver.exe")
    url = 'http://land.mk.co.kr/memul/list.php?bubcode=1135010300&mgroup=A&mclass=A01%2CA02%2CA03&bdiv=A&areadiv=&mseq=&JMJ='
    browser = webdriver.Chrome(path)
    browser.get(url)

    # 매매 버튼 클릭
    elem = browser.find_element_by_class_name("SearchType")
    elem = elem.find_elements_by_tag_name("dl")
    elem = elem[0].find_elements_by_tag_name("dd")
    elem = elem[0].find_elements_by_tag_name("ul")
    elem = elem[0].find_elements_by_tag_name("li")
    elem = elem[1].find_elements_by_tag_name('input')
    elem[0].click()

    # 조회하기 버튼 클릭
    elem = browser.find_element_by_class_name("Search")
    elem.click()

    #결과 저장할 배열들
    price = [] #가격
    space = [] #공급 면적
    kind = [] #매물 종류
    floor = [] #층수
    rooms = [] #방수
    year = [] #연식

    # 각 페이지 href 크롤링
    tables = browser.find_elements_by_class_name('TablePaginate')
    paginates = tables[0].find_elements_by_class_name('Paginate')
    target = paginates[0].find_elements_by_tag_name('a')
    target[-1].click()

    for item in range(0, 5):
        print("PAGE", item + 1)
        tables = browser.find_elements_by_class_name('TablePaginate')
        paginates = tables[0].find_elements_by_class_name('Paginate')
        target = paginates[0].find_elements_by_tag_name('a')
        target[item].click()

        # selenium으로 href속성 크롤링
        elem = browser.find_elements_by_class_name('AlignLeft')
        link = []  # 크롤링한 href를 저장할 배열
        for i in elem:
            elem = i.find_elements_by_class_name('Inner')
            elem = elem[0].find_elements_by_tag_name('a')
            result = elem[0].get_attribute('href')
            link.append(result[21:-2])

        # beautifulsoup으로 상세 정보 크롤링
        for i in link:
            url = 'http://land.mk.co.kr/memul/detail.php?bubcode=1135010300&mgroup=A&mclass=A01%2CA02%2CA03&bdiv=A&areadiv=&aptcode=&scalecode=&mseq={0}&xpos=&ypos=&tab=1&listOrder=&siteOrder=&JMJ='.format(
                i)
            req = requests.get(url)
            html = req.text
            soup = BeautifulSoup(html, 'html.parser')

            # 방수
            tds = soup.select('.ViewInfo td')[1]
            txt = tds.select('div')[0].text
            rooms.append(txt.split()[0])

            # 층수
            tds = soup.select('.ViewInfo td')[0]
            txt = tds.select('div')[0].text
            result = ''
            for s in txt:
                if s != '/':
                    # 저, 중, 고 로 나오는 값 랜덤값 부여
                    if s == '저':
                        floor.append(random.randrange(1, 11))
                        break
                    elif s == '중':
                        floor.append(random.randrange(11, 21))
                        break
                    elif s == '고':
                        floor.append(random.randrange(21, 31))
                        break
                    else:
                        result += s
                else:
                    floor.append(result)
                    break

            # 매물 종류
            # trs = soup.select('.DivDetail .DetailTable > table > tbody > tr')[5]
            # kind.append(trs.select('td > .Inner')[0].text)

            # 연식
            trs = soup.select('.DivDetail .DetailTable > table > tbody > tr')[7]
            year.append(trs.select('td > .Inner')[0].text[:-3])

            # 공급면적
            items = soup.select('.AreaZone > .RateInfo > span')
            result = ''
            for item in items:
                if (item.text != '/'):
                    result += item.text
                else:
                    break
            space.append(result)

            # 가격
            items = soup.select('.PriceZone > .RateInfo > span')
            result = ''
            for item in items:
                if item.text != ',' and item.text != '만원':
                    result += item.text

            price.append(result)

    def testCrawlRun(self):
        space = self.space
        #kind = self.kind
        floor = self.floor
        rooms = self.rooms
        year = self.year
        price = self.price
        return [space, floor, rooms, year, price]
