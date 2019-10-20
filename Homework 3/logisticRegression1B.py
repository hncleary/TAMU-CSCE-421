import numpy as np
from sklearn.datasets import make_classification
from matplotlib import pyplot as plt
from sklearn.linear_model import LogisticRegression
import seaborn as sns
sns.set()
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import pandas as pd


# def dataMatrixSplitTest(iteration, dataMatrix):
#
#     data = dataMatrix
#     rows = np.size(data, 0)
#     cols = np.size(data, 1)
#
#     numerator = iteration
#
# # create the split y train matrix
# # create the split x train matrix
# # create the split y test matrix
# # create the split x test matrix

def dataMatrixSplit(iteration, totalIterations, dataMatrix):
    data = dataMatrix
    rows = np.size(data, 0) - 1
    cols = np.size(data, 1)

    numerator = iteration
    denominator = totalIterations

    testSetRows = int(rows / denominator)
    trainSetRows = int(rows - testSetRows)
    # print(testSetRows)
    # print(trainSetRows)

    # building empty matrices for the TEST SETS
    buildX_TEST = np.zeros(shape=(testSetRows, cols - 1))
    buildY_TEST = np.zeros(shape=(testSetRows, 1))
    # building empty matrices for the TRAIN SETS
    buildX_TRAIN = np.zeros(shape=(trainSetRows, cols - 1))
    buildY_TRAIN = np.zeros(shape=(trainSetRows, 1))

    testStartRow = iteration*testSetRows + 1
    # print(testStartRow)
    # create the split x test matrix
    for i in range(testSetRows):
        # if i == 0:
        #     continue
        for j in range(np.size(buildX_TEST, 1)):
            currentValue = data.item(testStartRow + i, j)
            buildX_TEST.itemset((i, j), currentValue)
    # print(buildX_TEST)

    # create the split y test matrix
    for i in range(testSetRows):
        # if i == 0:
        #     continue
        currentValue = float( data.item(testStartRow + i, cols - 1) )
        if currentValue > 0:
            buildY_TEST.itemset((i, 0), 1)
        else:
            buildY_TEST.itemset((i, 0), 0)
    # print(buildY_TEST)

    # create the split x train matrix
    currentRowCount = 0
    testStartRowCountdown = testSetRows
    inTestSetRows = False
    for i in range(rows):
        # ignore the first line of strings
        if i == 0:
            continue
        #  continue if the training matrix has already been filled
        if currentRowCount == np.size(buildX_TRAIN, 0):
            continue
        # if iterator reaches the test start row
        if i == testStartRow:
            inTestSetRows = True
        # if all of the rows of been accounted for, continue to input data
        if testStartRowCountdown == 0:
            inTestSetRows = False
        #  count down the number of row iterated
        if inTestSetRows:
            testStartRowCountdown = testStartRowCountdown - 1
            continue
        else:
            for j in range(np.size(buildX_TRAIN, 1)):
                currentValue = data.item(i, j)
                buildX_TRAIN.itemset((currentRowCount, j), currentValue)
            # create the split y train matrix
            currentOutput = float( data.item(i, cols - 1) )
            # generate binary classes for the output array
            if currentOutput > 0:
                buildY_TRAIN.itemset((currentRowCount, 0), 1)
            else:
                buildY_TRAIN.itemset((currentRowCount, 0), 0)
            currentRowCount += 1
    # print(buildY_TRAIN)
    # print(np.size(buildY_TRAIN, 0), np.size(buildY_TRAIN, 1))
    return buildX_TRAIN, buildX_TEST, buildY_TRAIN, buildY_TEST



def logisticRegressionUsage(data_matrix, matrixRows, matrixCols):
    rows = matrixRows
    cols = matrixCols

    lr = LogisticRegression()


    return 0