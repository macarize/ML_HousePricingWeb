import numpy as np

class runMachine:
    X=[]
    Y=[]
    def runCostFuntion(self, Data, theta):
        J = 0
        m = Data.m
        colLen = len(Data.x[0])-1
        self.X = np.array(Data.x)
        self.Y = np.array(Data.y)

        j = np.sum(np.power(np.matmul(self.X, theta) - self.Y, colLen)) / (colLen * m)
        return J