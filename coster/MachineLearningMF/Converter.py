import sys
import numpy as np
sys.path.insert(0, '..\MachineLearningMF\crawl.py')
# import crawl
import re

class DataLoad:
    '''cl = crawl.crawl()'''

    qubic = []
    floor = []
    price = []
    ''''[qubic, floor, price] = cl.crawlRun()'''

    qubic = np.array(qubic)
    floor = np.array(floor)
    price = np.array(price)

    qubic = qubic.reshape(qubic.size, 1)
    floor = floor.reshape(floor.size, 1)
    price = price.reshape(price.size, 1)

    def Dataget(self):
        return [self.qubic, self.floor, self.price]

    def ConvertToCSV(self):
        self.price = np.concatenate((self.floor, self.price), axis=1)
        self.price = np.concatenate((self.qubic, self.price), axis=1)
        DataCSV = self.price
        np.savetxt("Data.txt", DataCSV, delimiter=",",fmt="%s")




