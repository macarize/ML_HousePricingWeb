import numpy as np
from MachineLearningMF import runMachine


class GradientDescent:
    ml = runMachine.runMachine()
    def runGradient(self, data , theta, alpha, iter):
        X = data.x
        Y = data.y
        m = data.m
        J_history = np.zeros((iter, 1),dtype=int)


        for i in range(0, iter):
            error = np.matmul(X, theta)
            error = np.subtract(error,Y)
            gradient = np.dot(X.transpose(), error)
            theta = theta - alpha * gradient / m

            J_history[i] = self.ml.runCostFuntion(data, theta)
        return theta
