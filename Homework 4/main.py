import numpy as np
import csv as csv
import pandas as pd
import sklearn as sklearn
import seaborn as sns
import matplotlib.pyplot as plt

# extra imports
import helperFunctions as hf
# regressor import
from sklearn.tree import DecisionTreeRegressor

trainData = pd.read_csv("OnlineNewsPopularityTrain.csv")
testData = pd.read_csv("OnlineNewsPopularityTest.csv")

XTrain, YTrain = hf.parseFullDataframe(trainData)
XTest, YTest = hf.parseFullDataframe(testData)

print(hf.randomizeFeatureSet(XTrain, XTest))

# height is depth variations (10)
# width is random tree count (7)
errorMatrix = np.zeros((10, 7))
kValues = []
treeCount = 0
for k in range(7):
    treeCount = treeCount + 1
    depthDeciding = False
    # arrays for plotting depths vs averages at that depth
    depths = []
    errorAverages = []
    depth = 20
    loopCount = 0
    while depthDeciding:
        loopCount = loopCount + 1
        regressor = DecisionTreeRegressor(random_state=0, max_depth=depth)
        errorArray = []
        for i in range(5):
            # split for cross fold validation
            splitTrainInput, splitTrainOutput, splitTestInput, splitTestOutput = hf.fiveFoldCrossValidation(i, trainData)
            for j in range(treeCount):
                # select random features for the set
                splitTrainInputNew, splitTestInputNew = hf.randomizeFeatureSet(splitTrainInput, splitTestInput)
                # train the values on the 4/5
                regressor.fit(splitTrainInputNew, splitTrainOutput)
                # predict the values on the the 1/5
                prediction = np.array(regressor.predict(splitTestInputNew))
                actualValues = hf.parseOutputDataFrame(splitTestOutput)
                # calculate the error for the current fold
                RSSError = hf.errorCalcRSS(prediction, actualValues)
                errorArray.append(RSSError)
        errorAverage = hf.arrayAverage(errorArray)
        # print(errorAverage)
        errorAverages.append(errorAverage)
        depths.append(depth)
        kValues.append(k)

        errorMatrix.itemset((loopCount - 1, k), errorAverage)
        print("Data Value Added to Matrix", errorAverage)

        print("depthIncreased to ", depth)
        depth = depth + 5
        if depth > 65:
            depthDeciding = False

# print(min(errorAverages))
# print(depths[errorAverages.index(min(errorAverages))])
# print(kValues[errorAverages.index(min(errorAverages))])


treeCount2 = 5
errorAverages2 = []
regressor2 = DecisionTreeRegressor(random_state=0, max_depth=65)
for j in range(treeCount2):
    XTrainNew, XTestNew = hf.randomizeFeatureSet(XTrain, XTest)
    regressor2.fit(XTrainNew, YTrain)
    prediction2 = np.array(regressor2.predict(XTestNew))
    actualValues2 = hf.parseOutputDataFrame(YTest)
    RSSError2 = hf.errorCalcRSS(prediction2, actualValues2)
    errorAverages.append(RSSError2)
print(hf.arrayAverage(errorAverages))

# plt.plot(depths, errorAverages)
# plt.ylabel("RSS Error Average")
# plt.xlabel("Depth")
# plt.show()

# fig, ax = plt.subplots()
#
# min_val = min(errorAverages)
# max_val = max(errorAverages)
#
# # intersection_matrix = np.random.randint(0, 10, size=(max_val, max_val))
#
# ax.matshow(errorMatrix, cmap=plt.cm.Blues)
#
# for i in range(7):
#     for j in range(10):
#         c = errorMatrix[j, i]
#         # ax.text(i, j, str(c), va='center', ha='center')
#
# plt.show()