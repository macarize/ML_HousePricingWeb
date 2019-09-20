from MachineLearningMF import DataInit, AddBias, GradientDescent, Normalization, Converter, runMachine
import os.path
import numpy as np


def ml(year,rooms,floor,space):
    BASE = os.path.dirname(os.path.abspath(__file__))

    print(os.path.join(BASE, "DataNew.csv"))
    Path = os.path.join(BASE, "DataNew.csv")

    # Path = "..\MachineLearningMF\Data.txt"

    '''somethin somthin'''
    data = DataInit.DataInit()
    CostFuntion = runMachine.runMachine()
    GDescent = GradientDescent.GradientDescent()
    Norm = Normalization.Normalization()
    AddBias1 = AddBias.AddBias()

    '''loac cvs'''
    data.loader(Path)
    '''theta init'''
    '''initiated optimal theta 17/9/2019'''
    theta = np.array([[39656.8149943], [2839.62957553], [4611.727268], [998.44858994], [7378.01918862]])
    '''Normalize'''
    data.x, mu, sigma = Norm.featureNormalize(data)
    '''Add Bias Column'''
    data = AddBias1.addB(data)
    '''remove annotations when you compute theta again'''
    '''run Gradient descent and Cost function'''
    '''theta = GDescent.runGradient(data,theta,0.0001,100000)
    theta = theta.reshape(1, 5)'''

    '''compute housing price'''
    r = np.array([year,rooms,floor,space])

    r = r.astype(float)
    mu = mu.astype(float)
    sigma = sigma.astype(float)

    r = (r - mu)/sigma
    r2 = np.ones(r.shape[0]+1)
    r2[1:] = r
    r = r2
    price = np.dot(r.reshape(1,5), theta.reshape(5,1))
    print('\nPredicted price of a 1650 sq-ft, 3 br house (using gradient descent): ', price[0][0])
    print(theta)
    return price[0][0]


ml(2002,4,12,165.47)
#cl = Converter.DataLoad()
#cl.ConvertToCSV()


