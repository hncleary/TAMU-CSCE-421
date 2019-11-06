import numpy as np
import csv as csv
import pandas as pd
import sklearn as sklearn
import seaborn as sns
import matplotlib.pyplot as plt
import random


def randomizeFeatureSet(splitTrainInput, splitTestInput):
    splitTrainX,  splitTestX = splitTrainInput, splitTestInput

    randNum = random.randint(1, 7)
    featureBegin = randNum*5
    featureEnd = featureBegin + 20

    splitTrainXNew = splitTrainX.iloc[:, 1+featureBegin:featureEnd].astype(float)
    splitTestXNew = splitTestX.iloc[:, 1+featureBegin:featureEnd].astype(float)

    return splitTrainXNew, splitTestXNew


def arrayAverage(array):
    total = 0
    for i in range(len(array)):
        total = total + array[i]
    average = total / len(array)
    return average


def errorCalcRSS(prediction, actualValues):
    error = 0
    RSSError = 0
    for i in range(len(prediction)):
        currentValue = (actualValues[i] - prediction[i]) ** 2
        RSSError = RSSError + currentValue
    return RSSError


def parseOutputDataFrame(Y):
    yNumpyArray = np.array(Y.to_numpy().transpose())
    array = []
    for i in range(np.size(yNumpyArray)):
        array.append(yNumpyArray[0, i])
    array = np.array(array)
    return array


def parseFullDataframe(dataFrame):
    # input features minus the URL
    X = dataFrame.iloc[:, 1:60].astype(float)
    # output value (shares)
    Y = dataFrame.iloc[:, 60:61].astype(float)

    return X, Y


def fiveFoldCrossValidation(currentIteration, dataFrame):
    # data = dataFrame.toNumpy()
    iteration = currentIteration

    dataRows = dataFrame.shape[0]
    dataCols = dataFrame.shape[1]

    # number of rows that each test cross section will have
    rowsInSection = int(dataRows / 5)
    rowStart = rowsInSection * currentIteration

    if currentIteration == 0:
        splitTrainInput = dataFrame.iloc[rowsInSection:dataRows, 1:60].astype(float)
        splitTrainOutput = dataFrame.iloc[rowsInSection:dataRows, 60:61].astype(float)

        splitTestInput = dataFrame.iloc[0:rowsInSection, 1:60].astype(float)
        splitTestOutput = dataFrame.iloc[0:rowsInSection, 60:61].astype(float)

    elif currentIteration == 4:
        splitTrainInput = dataFrame.iloc[0:dataRows-rowsInSection, 1:60].astype(float)
        splitTrainOutput = dataFrame.iloc[0:dataRows-rowsInSection, 60:61].astype(float)

        splitTestInput = dataFrame.iloc[dataRows-rowsInSection:dataRows, 1:60].astype(float)
        splitTestOutput = dataFrame.iloc[dataRows-rowsInSection:dataRows, 60:61].astype(float)

    else:
        splitTrainInput1 = dataFrame.iloc[0:rowStart, 1:60].astype(float)
        splitTrainOutput1 = dataFrame.iloc[0:rowStart, 60:61].astype(float)

        splitTrainInput2 = dataFrame.iloc[rowStart+rowsInSection:dataRows, 1:60].astype(float)
        splitTrainOutput2 = dataFrame.iloc[rowStart+rowsInSection:dataRows, 60:61].astype(float)

        splitTrainInput = splitTrainInput1.append(splitTrainInput2)
        splitTrainOutput = splitTrainOutput1.append(splitTrainOutput2)

        splitTestInput = dataFrame.iloc[rowStart:rowStart+rowsInSection, 1:60].astype(float)
        splitTestOutput = dataFrame.iloc[rowStart:rowStart+rowsInSection, 60:61].astype(float)

    # needs to return the 1/5 testing matrix
    # and the 4/5 training matrix
    return splitTrainInput, splitTrainOutput, splitTestInput, splitTestOutput
