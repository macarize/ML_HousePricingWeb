import numpy as np
<<<<<<< Updated upstream
sys.path.insert(0, '..\MachineLearningMF\crawl.py')
import crawl
import re
=======
import pandas as pd
import testCrawl
>>>>>>> Stashed changes


class DataLoad:
    '''remove followed annotation when you want to crawl data again'''
    '''cl = testCrawl.testCrawl()'''
    space = []
    '''annotated because we will treat this by saving files seperatly'''
    '''kind = []'''
    floor = []
    rooms = []
    year = []
    price = []

    #[space, floor, rooms, year, price] = cl.testCrawlRun()

    space = np.array(space)
    '''annotated because we will treat this by saving files seperatly'''
    '''kind = np.array(kind)'''
    floor = np.array(floor)
    rooms = np.array(rooms)
    year = np.array(year)
    price = np.array(price)

    n = price.size

    space = space.reshape(n, 1)
    '''annotated because we will treat this by saving files seperatly'''
    '''''''#kind = kind.reshape(n, 1)'''
    floor = floor.reshape(n, 1)
    rooms = rooms.reshape(n, 1)
    year = year.reshape(n, 1)
    price = price.reshape(n, 1)


    def Dataget(self):
        return [self.space, self.floor,
                self.rooms, self.year, self.price]

    def ConvertToCSV(self):
        self.price = np.concatenate((self.space, self.price), axis=1)
        '''annotated because we will treat this by saving files seperatly'''
        '''elf.price = np.concatenate((self.kind, self.price), axis=1)'''
        self.price = np.concatenate((self.floor, self.price), axis=1)
        self.price = np.concatenate((self.rooms, self.price), axis=1)
        self.price = np.concatenate((self.year, self.price), axis=1)
        DataCSV = self.price
        '''annotated because there was conflicting encoding problems'''
        '''np.savetxt("DataNew.txt", DataCSV.encode('utf8'), delimiter=",", fmt="%s")'''
        pd.DataFrame(DataCSV).to_csv("DataNew.csv", index=False, header=False)


    '''annotated becaouse there were enough testing'''
    '''# 가격 결과 출력
    print("price : ", price)
    print("price(len) : ", len(price))
    # 공급면적 결과 출력
    print("space : ", space)
    print("space(len) : ", len(space))
    # 매물종류 결과 출력
    #print("kind : ", kind)
    #print("kind(len) : ", len(kind))
    # 층수 결과 출력
    print("floor : ", floor)
    print("floor(len) : ", len(floor))
    # 방수 결과 출력
    print("rooms : ", rooms)
    print("rooms(len) : ", len(rooms))
    # 연식 결과 출력
    print("year : ", year)
    print("year(len) : ", len(year))'''


