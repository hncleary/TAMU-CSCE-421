import numpy as np
import csv as csv
import pandas as pd
import sklearn as sklearn
import seaborn as sns
import matplotlib.pyplot as plt
import math as math

print ("Numpy Version: " , (np.__version__))
print ("CSV Version: " , (csv.__version__))
print ("Pandas Version: " , (pd.__version__))
print ("Sci-Kit-Learn Version: " , (sklearn.__version__))
print ("Seaborn Version: " , (sns.__version__))


# with open("hw3_question2.csv") as csvQuestion2:
#     reader = csv.DictReader(csvQuestion2)
#     Question2_table = [row.split(",") for row in csvQuestion2.read().replace("\r", "").split("\n")]
#     Question2_matrix = np.matrix(Question2_table)
# Question2Rows = np.size(Question2_matrix, 0)
# Question2Cols = np.size(Question2_matrix, 1)

data = pd.read_csv('hw3_question2.csv')
# print(data.head())
# print(data.shape[0])

#  Question 2-i -- Plot the number of tickets sold over the two years
from Question2Plotting import dataTicketsSold, dataTicketsSoldFirstMonth, plotValues
# plotTicketsSold(data)
X, Y = dataTicketsSoldFirstMonth(data)
# plotValues(X, Y)

#  Question 2-ii poisson model
import Question2Poisson as Q2P
# lambdaVal = sum(Y)/len(Y)
# lambdaVal = 6
# poissonModel = Q2P.poissonModel(lambdaVal, Y)
# print(poissonModel)
test = Q2P.poissonEquation(6, Y)
YMinimum = min(Y)
YMaximum = max(Y)
YProb = []
YLabels = []
for i in range(int(YMinimum), int(YMaximum)):
    YLabels.append(i)
    YProb.append(Q2P.poissonEquation(i, Y))

plt.plot(YLabels, YProb)
plt.ylabel("Probability During Each Hour")
plt.xlabel("Values")
plt.show()

# from Question2Max import MLEFunction
# MLEFunction(X, Y)