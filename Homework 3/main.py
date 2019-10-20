import numpy as np
import csv as csv
import pandas as pd
import sklearn as sklearn
import seaborn as sns
import matplotlib.pyplot as plt

print ("Numpy Version: " , (np.__version__))
print ("CSV Version: " , (csv.__version__))
print ("Pandas Version: " , (pd.__version__))
print ("Sci-Kit-Learn Version: " , (sklearn.__version__))
print ("Seaborn Version: " , (sns.__version__))

with open("hw3_question1.csv") as csvQuestion1:
    reader = csv.DictReader(csvQuestion1)
    Question1_table = [row.split(",") for row in csvQuestion1.read().replace("\r", "").split("\n")]
    Question1_matrix = np.matrix(Question1_table)
Question1Rows = np.size(Question1_matrix, 0)
Question1Cols = np.size(Question1_matrix, 1)


with open("hw3_question2.csv") as csvQuestion2:
    reader = csv.DictReader(csvQuestion2)
    Question2_table = [row.split(",") for row in csvQuestion2.read().replace("\r", "").split("\n")]
    Question2_matrix = np.matrix(Question1_table)
Question2Rows = np.size(Question1_matrix, 0)
Question2Cols = np.size(Question1_matrix, 1)


# Question 1-A
# Plot a histogram of the outcome variable
PlotQuestion1 = False
if PlotQuestion1:
    from outcomeHistogramPlot import outcomeHistogramPlot
    outcomeHistogramPlot(Question1_matrix, Question1Rows, Question1Cols)


# Question 1-B
# dichotomize the outcome variable
# Class 0 -- x=0, Forests not affected by the fire
# Class 1 -- x>0, Forests affected by the fire

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from logisticRegression1B import dataMatrixSplit
# # cross validate the logistic regression using implemented 10-fold cross-validation
#
# # 10-fold cross-validation matrices generation
for i in range(10):
    X_train, X_test, Y_train, Y_test = dataMatrixSplit(i, 10, Question1_matrix)
    #  create an instance of linear regression and fit the model
    logmodel = LogisticRegression(solver='liblinear', multi_class='auto')
    logmodel.fit(X_train, Y_train.ravel() )

    predictions = logmodel.predict(X_test)
    # print(i)
    # print(classification_report(Y_test.round() , predictions.round() ))
    sns.regplot()



precisionArray = [.5, .5, .6, .5, .54, .47, .48, .53, .56, .46]
summify = 0
for i in range(len(precisionArray)):
    summify += precisionArray[i]
average = summify / len(precisionArray)
print(average)


# train = pd.read_csv('hw3_question1.csv')

# X = train[['X', 'Y', 'month', 'day', 'FFMC', 'DMC', 'DC', 'ISI', 'temp', 'RH', 'wind', 'rain']]
# Y = train['area']

# X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, random_state=101)

# lab_enc = preprocessing.LabelEncoder()
# Y_train = lab_enc.fit_transform(Y_train)
#
# lab_enc2 = preprocessing.LabelEncoder()
# Y_test = lab_enc2.fit_transform(Y_test)

