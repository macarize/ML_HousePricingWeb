from MachineLearningMF import DataInit, AddBias, GradientDescent, Normalization, Converter, runMachine
import os.path
import numpy as np


def ml(year,rooms,floor,space):
    BASE = os.path.dirname(os.path.abspath(__file__))

    print(os.path.join(BASE, "DataNew.txt"))
    Path = os.path.join(BASE, "DataNew.txt")
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
    theta = np.array([[43000.01475504], [2504.21369816], [5321.04358409], [-613.123852], [4505.00713087]])
    '''Normalize'''
    data.x, mu, sigma = Norm.featureNormalize(data)
    '''Add Bias Column'''
    data = AddBias1.addB(data)
    '''remove annotations when you compute theta again'''
    '''run Gradient descent and Cost funtion'''
    '''theta = GDescent.runGradient(data,theta,0.001,100000)
    theta = theta.reshape(1, 5)'''

    '''compute housing price'''
    r = np.array([year,rooms,floor,space])
    r = (r - mu)/sigma
    r2 = np.ones(r.shape[0]+1)
    r2[1:] = r
    r = r2
    price = np.dot(r.reshape(1,5), theta.reshape(5,1))
    print('\nPredicted price of a 1650 sq-ft, 3 br house (using gradient descent): ', price[0][0])
    return price[0][0]

ml(2001,3,1,77.68)


#cl = Converter.DataLoad()
#cl.ConvertToCSV()
