import DataInit, AddBias, GradientDescent, Normalization, runMachine
import os.path
import numpy as np


BASE = os.path.dirname(os.path.abspath(__file__))

print(os.path.join(BASE, "DataNew1.csv"))
Path = os.path.join(BASE, "DataNew1.csv")

# Path = "..\MachineLearningMF\Data.txt"

'''somethin somthin'''
data = DataInit.DataInit()
CostFuntion = runMachine.runMachine()
GDescent = GradientDescent.GradientDescent()
Norm = Normalization.Normalization()
AddBias1 = AddBias.AddBias()

'''loac csv'''
data.loader(Path) # ,제거
'''theta init'''
'''initiated optimal theta 17/9/2019'''
# 동 별 theta값 입력 테스트
# theta = np.array([[theta0], [theta1], [theta2], [theta3], [theta4]])
theta = np.array([[0], [0], [0], [0], [0]])
'''Normalize'''
data.x, mu, sigma = Norm.featureNormalize(data)
'''Add Bias Column'''
data = AddBias1.addB(data)
'''remove annotations when you compute theta again'''
'''run Gradient descent and Cost function'''
theta = GDescent.runGradient(data,theta,0.0001,100000) #theta값 뽑아내기
theta = theta.reshape(1, 5) #행렬 곱셈하기 위해 형태바꾸기
print(theta)

# cl = Converter.DataLoad()
# cl.ConvertToCSV()