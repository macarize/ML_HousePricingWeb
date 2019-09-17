from MachineLearningMF import DataInit, AddBias, GradientDescent, Normalization, Converter, runMachine

<<<<<<< Updated upstream
import numpy as np


Path = "..\MachineLearningMF\Data.txt"

'''somethin somthin'''
data = DataInit.DataInit()
CostFuntion = runMachine.runMachine()
GDescent = GradientDescent.GradientDescent()
Norm = Normalization.Normalization()
AddBias = AddBias.AddBias()

'''loac cvs'''
data.loader(Path)
'''theta init'''
theta = np.array([[42153.26281424], [13181.59072893],  [3297.21572782]])
'''Normalize'''
data.x, mu, sigma = Norm.featureNormalize(data)
'''Add Bias Column'''
data = AddBias.addB(data)
'''run Gradient descent and Cost funtion'''
'''theta = GDescent.runGradient(data,theta,0.0001,100000)'''
J = CostFuntion.runCostFuntion(data, theta)
theta = theta.reshape(1,3)

'''computied theta'''
print('Computed theta : {}'.format(theta))

'''predicting housing price'''
r = np.array([51.55, 15])
r = (r - mu) / sigma
r2 = np.ones(r.shape[0] + 1)
r2[1:] = r
r = r2
price = np.dot(r.reshape(1,3), theta.transpose())
string = "Predicted price of a 1650 sq-ft, 3 br house (using gradient descent): " + str(price[0][0])
print(string)
print(theta)
# cl = Converter.DataLoad()
# cl.ConvertToCSV()
=======
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

>>>>>>> Stashed changes

