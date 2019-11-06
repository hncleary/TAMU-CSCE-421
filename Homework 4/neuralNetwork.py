import numpy as np
import csv as csv
import pandas as pd
import sklearn as sklearn
import seaborn as sns
import matplotlib.pyplot as plt

# extra imports
import helperFunctions as hf
from sklearn.neural_network import MLPClassifier

trainData = pd.read_csv("OnlineNewsPopularityTrain.csv")
testData = pd.read_csv("OnlineNewsPopularityTest.csv")

XTrain, YTrain = hf.parseFullDataframe(trainData)
XTest, YTest = hf.parseFullDataframe(testData)

YTrainArray = hf.parseOutputDataFrame(YTrain)
YTestArray = hf.parseOutputDataFrame(YTest)

errorArray = []

multiLayerPerceptron = MLPClassifier(solver='lbfgs', alpha=1e-5, random_state=1, max_iter=100, hidden_layer_sizes=(15,))
for i in range(5):
    # split original train data for cross fold validation
    splitTrainInput, splitTrainOutput, splitTestInput, splitTestOutput = hf.fiveFoldCrossValidation(i, trainData)
    YTrainSplitArray = hf.parseOutputDataFrame(splitTrainOutput)
    YTestSplitArray = hf.parseOutputDataFrame(splitTestOutput)

    # # specify feature input
    # splitTrainInput, splitTestInput = hf.specifyFeatureSet(splitTrainInput, splitTestOutput)

    # fit the MLP model
    print("MLP Fit", i, " Started")
    multiLayerPerceptron.fit(splitTrainInput, YTrainSplitArray)
    print("MLP Fit", i, " Complete")
    # predictions for current fit
    predictions = multiLayerPerceptron.predict(XTest)
    # RSS Error for Current Predictions
    RSSError = hf.errorCalcRSS(predictions, YTestSplitArray)
    errorArray.append(RSSError)

averageError = hf.arrayAverage(errorArray)

print(errorArray)
print(averageError)