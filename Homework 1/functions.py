import math

def euclideanDistance(x,y):
    distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
    return distance


def knnClassifier(kValue, dataPoint, dataMatrix):
    k = kValue
    x, y = dataPoint

    matrixRows = dataMatrix

    return 0