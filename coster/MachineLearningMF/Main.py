from MachineLearningMF import DataInit, AddBias, GradientDescent, Normalization, Converter, runMachine
import os.path
import numpy as np

def ml(space, floor):
    BASE = os.path.dirname(os.path.abspath(__file__))

    print(os.path.join(BASE, "Data.txt"))
    Path = os.path.join(BASE, "Data.txt")
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
    theta = np.array([[42153.26281424], [13181.59072893], [3297.21572782]])
    '''Normalize'''
    data.x, mu, sigma = Norm.featureNormalize(data)
    print(Norm.featureNormalize(data))
    '''Add Bias Column'''
    data = AddBias1.addB(data)
    '''run Gradient descent and Cost funtion'''
    '''theta = GDescent.runGradient(data,theta,0.0001,100000)'''
    J = CostFuntion.runCostFuntion(data, theta)
    theta = theta.reshape(1, 3)

    '''computied theta'''
    print('Computed theta : {}'.format(theta))

    '''predicting housing price'''
    r = np.array([space, floor])
    r = r.astype(float)
    mu = mu.astype(float)
    sigma = sigma.astype(float)

    r = np.divide(np.subtract(r, mu), sigma)
    r2 = np.ones(r.shape[0] + 1)
    r2[1:] = r
    r = r2
    price = np.dot(r.reshape(1, 3), theta.transpose())
    string = "Predicted price of a 1650 sq-ft, 3 br house (using gradient descent): " + str(price[0][0])
    print(string)
    print(theta)
    return str(price[0][0])
    # cl = Converter.DataLoad()
    # cl.ConvertToCSV()

