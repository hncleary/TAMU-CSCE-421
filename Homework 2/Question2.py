import numpy as np
import csv as csv
print "Numpy Version: ", (np.__version__)
print "CSV Version: ", (csv.__version__)

with open("airfoil_self_noise_test.csv") as csvNoiseTest:
    reader = csv.DictReader(csvNoiseTest)
    noiseTest_table = [row.split(",") for row in csvNoiseTest.read().replace("\r", "").split("\n")]
    noiseTest_matrix = np.matrix(noiseTest_table)
noiseTestRows = np.size(noiseTest_matrix, 0)
noiseTestCols = np.size(noiseTest_matrix, 1)

with open("airfoil_self_noise_train.csv") as csvNoiseTrain:
    reader = csv.DictReader(csvNoiseTrain)
    noiseTrain_table = [row.split(",") for row in csvNoiseTrain.read().replace("\r", "").split("\n")]
    noiseTrain_matrix = np.matrix(noiseTrain_table)
noiseTrainRows = np.size(noiseTrain_matrix, 0)
noiseTrainCols = np.size(noiseTrain_matrix, 1)

# print noiseTestCols, noiseTestRows
# print noiseTrainCols, noiseTrainRows

# print noiseTrain_matrix.item(2,0)

# Question (i) - Plotting Histograms
from histogramPlot import histogramPlot
# histogramPlot(noiseTrain_matrix, noiseTrainRows, noiseTrainCols)

# Question (ii) - Linear Regression (OLS)
# build data matrix and output matrix
from linearRegression import buildDataMatrix
dataMatrix = buildDataMatrix(noiseTrain_matrix, noiseTrainRows, noiseTrainCols)

from linearRegression import buildOutputMatrix
outputMatrix = buildOutputMatrix(noiseTrain_matrix, noiseTrainRows, noiseTrainCols)


from linearRegression import ordinaryLeastSquares
weights = ordinaryLeastSquares(dataMatrix, outputMatrix)
print weights

from linearRegression import RSS
RSSValue = RSS(dataMatrix, outputMatrix, weights)

testMatrix = buildDataMatrix(noiseTest_matrix, noiseTestRows, noiseTrainCols)
testOutputMatrix = buildOutputMatrix(noiseTest_matrix, noiseTestRows, noiseTestCols)
testRSSValue = RSS(testMatrix, testOutputMatrix, weights)

print testRSSValue


from linearRegression import buildCustomDataMatrix

dataMatrix2 = buildCustomDataMatrix(noiseTrain_matrix)
testMatrix2 = buildCustomDataMatrix(noiseTest_matrix)
# print dataMatrix2
# print np.shape(dataMatrix2)

weights2 = ordinaryLeastSquares(dataMatrix2, outputMatrix)
print weights2

RSSValue2 = RSS(testMatrix2, testOutputMatrix, weights2)
print RSSValue2


# find the relationship between inputs and ouputs using ordinary least squares
# from linearRegression import linearRegression
# # linear regression function returns a vector of weights to correspond features with output
# weights = linearRegression(dataMatrix, outputMatrix)
# print weights

# from linearRegression import ordinaryLeastSquares
#
# weights2 = ordinaryLeastSquares(dataMatrix, outputMatrix)
# print weights2

# from linearRegression import testModel
# modelTest = testModel(weights, noiseTest_matrix)
# print modelTest

