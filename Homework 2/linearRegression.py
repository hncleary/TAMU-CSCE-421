import numpy as np
import csv as csv
import pandas as pd
print "Numpy Version: " , (np.__version__)
print "CSV Version: " , (csv.__version__)
print "Pandas Version: " , (pd.__version__)


def buildDataMatrix(dataMatrix, matrixRows, matrixCols):
    rows = matrixRows
    cols = matrixCols
    buildMatrix = np.zeros(shape=(rows, cols))
    for i in range(rows):
        for j in range(cols):
            if j == 0:
                buildMatrix.itemset((i, j), 1)
            else:
                currentValue = float(dataMatrix.item(i, j-1))
                buildMatrix.itemset((i, j), currentValue)
    # print buildMatrix
    return buildMatrix


def buildCustomDataMatrix(dataMatrix):
    rows = np.size(dataMatrix, 0)
    cols = np.size(dataMatrix, 1)
    parameters = 1
    parameterTruths  = np.zeros(shape=(1, cols))
    include1 = True
    include2 = True
    include3 = False
    include4 = True
    include5 = True

    parameterTruths.itemset(0, 1)
    if include1:
        parameters += 1
        parameterTruths.itemset(1, 1)
    if include2:
        parameters += 1
        parameterTruths.itemset(2, 1)
    if include3:
        parameters += 1
        parameterTruths.itemset(3, 1)
    if include4:
        parameters += 1
        parameterTruths.itemset(4, 1)
    if include5:
        parameters += 1
        parameterTruths.itemset(5, 1)

    buildMatrix = np.zeros(shape=(rows, parameters))
    for i in range(rows):
        generatedCols = 0
        for j in range(cols):
            if j == 0:
                buildMatrix.itemset((i, j), 1)
                generatedCols += 1
            elif j == 1 and include1:
                currentValue = float(dataMatrix.item(i, j - 1))
                buildMatrix.itemset((i, generatedCols), currentValue)
                generatedCols += 1
            elif j == 2 and include2:
                currentValue = float(dataMatrix.item(i, j - 1))
                buildMatrix.itemset((i, generatedCols), currentValue)
                generatedCols += 1
            elif j == 3 and include3:
                currentValue = float(dataMatrix.item(i, j - 1))
                buildMatrix.itemset((i, generatedCols), currentValue)
                generatedCols += 1
            elif j == 4 and include4:
                currentValue = float(dataMatrix.item(i, j - 1))
                buildMatrix.itemset((i, generatedCols), currentValue)
                generatedCols += 1
            elif j == 5 and include5:
                currentValue = float(dataMatrix.item(i, j - 1))
                buildMatrix.itemset((i, generatedCols), currentValue)
                generatedCols += 1
            # else:
            #     currentValue = float(dataMatrix.item(i, j - 1))
            #     buildMatrix.itemset((i, j), currentValue)

    print parameters
    print parameterTruths

    return buildMatrix




def buildOutputMatrix(dataMatrix, matrixRows, matrixCols):
    rows = matrixRows
    cols = matrixCols

    buildMatrix = np.zeros(shape=(rows, 1))

    for i in range(rows):
        currentValue = float(dataMatrix.item(i,5))
        buildMatrix.itemset((i,0), currentValue)

    return buildMatrix
def buildOutputArray(outputMatrix):
    outputArray = []
    rows = np.size(outputMatrix, 0)
    for i in range(rows):
        currentValue = outputMatrix.item(i,0)
        outputArray.append(currentValue)

    return outputArray


def arrayAverage(array):
    return sum(array) / len(array)

def arraySquareSummation(array):
    squareSum = 0
    for i in range(len(array)):
        currentValue = array[i]**2
        squareSum = squareSum + currentValue
    return squareSum

def featureArray(inputMatrix, featureNum):
    rows = np.size(inputMatrix, 0)
    featureArray = []

    for i in range(rows):
        currentVal = inputMatrix.item(i, featureNum)
        featureArray.append(currentVal)

    # average = arrayAverage(featureArray)
    return featureArray


#function will return array of d weights that correlate input and output data matrices
def linearRegression(inputMatrix, outputMatrix):
    dataMatrixRows = np.size(inputMatrix, 0)
    dataMatrixCols = np.size(inputMatrix, 1)
    # 650 rows , 6 columns
    # output matrix has 1 column and an equal number of rows
    weightsVector = np.zeros(shape=(1, dataMatrixCols))
    print weightsVector
    # find the average y
    outputArray = buildOutputArray(outputMatrix)
    outputAverage = arrayAverage(outputArray)
    # for each feature in the data-set / input matrix
    # for each weight possible in the weight vector
    for i in range(dataMatrixCols):
        # do not perform weight calculation for the bias
        if i == 0:
            continue
        currentWeight = 0
        # calculate numerator
        currentFeatureArray = featureArray(inputMatrix, i)
        # xn * yn sum
        xySum = 0
        for k in range( dataMatrixRows ):
            currentXY = currentFeatureArray[k]*outputArray[k]
            xySum = xySum + currentXY
        subtractVal = 0
        currentFeatureAverage = arrayAverage(currentFeatureArray)
        subtractVal = (len(currentFeatureArray) * currentFeatureAverage * outputAverage)
        topSectionVal = xySum - subtractVal
        # calculate divisor
        squareSum = arraySquareSummation(currentFeatureArray)
        subtractVal2 = dataMatrixRows*currentFeatureAverage
        bottomSectionVal = squareSum - subtractVal2

        currentWeight = topSectionVal / bottomSectionVal
        weightsVector.itemset(i, currentWeight)
    # computing the first weight (w0) of the weightsVector
    currentFeatureArray = featureArray(inputMatrix, 1)
    aa = arrayAverage(currentFeatureArray)
    weight0 = outputAverage - (weightsVector.item(1) * aa)
    weightsVector.itemset(0, weight0)

    return weightsVector

def ordinaryLeastSquares(dataMatrix, outputMatrix):
    data = dataMatrix
    output = outputMatrix

    transposeData = np.transpose(data)

    insideParenthesis = transposeData.dot(data)
    invertedParenthesis = np.linalg.inv(insideParenthesis)
    beforeOutputMult = invertedParenthesis.dot(transposeData)
    final = beforeOutputMult.dot(outputMatrix)
    return final

def testModel(weightsMatrix, testMatrix):
    weights = weightsMatrix
    model = testMatrix

    modelRows = np.size(testMatrix, 0)
    modelCols = np.size(testMatrix, 1)

    estimatedValueArray = []
    for i in range(modelRows):
        estimatedValue = 0
        for j in range(modelCols - 1):

            if j == 0:
                estimatedValue = estimatedValue + weights.item(1)
        else:
            currentValue = float(weights.item(j)) * float(testMatrix.item((i, j)))
            estimatedValue = estimatedValue + currentValue
        estimatedValueArray.append(estimatedValue)
    return estimatedValueArray

def RSS(dataMatrix, outputMatrix, weightsMatrix):
    weights = weightsMatrix
    data = dataMatrix
    output = outputMatrix

    dataTimesWeights = data.dot(weights)
    firstParenthesis = np.subtract(output,dataTimesWeights)
    firstParenthesisTranspose = np.transpose(firstParenthesis)

    square = firstParenthesisTranspose.dot(firstParenthesis)
    return square






