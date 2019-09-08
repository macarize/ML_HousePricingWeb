import DataInit
import AddBias
import runMachine
import GradientDescent
import Normalization
import numpy as np
import matplotlib.pyplot as plt


Path = "C:\\Users\leehy\PycharmProjects\MachineLearningMF\ex1data2.txt"

'''somethin somthin'''
data = DataInit.DataInit()
CostFuntion = runMachine.runMachine()
GDescent = GradientDescent.GradientDescent()
Norm = Normalization.Normalization()
AddBias = AddBias.AddBias()

'''loac cvs'''
data.loader(Path)
'''theta init'''
theta = np.array([[0], [0], [0]])
'''Normalize'''
data.x, mu, sigma = Norm.featureNormalize(data)
'''Add Bias Column'''
data = AddBias.addB(data)
'''run Gradient descent and Cost funtion'''
theta = GDescent.runGradient(data,theta,0.01,400)
J = CostFuntion.runCostFuntion(data, theta)
theta = theta.reshape(1,3)

'''computied theta'''
print('Computed theta : {}'.format(theta))

'''predicting housing price'''
r = np.array([1650, 3])
r = (r - mu) / sigma
r2 = np.ones(r.shape[0] + 1)
r2[1:] = r
r = r2
price = np.dot(r.reshape(1,3), theta.transpose())
string = "Predicted price of a 1650 sq-ft, 3 br house (using gradient descent): " + str(price[0][0])
print(string)



