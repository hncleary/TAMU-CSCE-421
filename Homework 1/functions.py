import scipy.spatial.distance as dist
import numpy as np
import math
import operator

def euclideanDistance(x,y):
    distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
    return distance

def sciPyEuclideanDistance(x,y):
    return dist.euclidean(x,y)

def manhattanDistance(x,y):
    return dist.cityblock(x,y)

def cosineSimilarity(x,y):
    return dist.cosine(x,y)

def chebyshevDistance(x,y):
    return dist.chebyshev(x,y)

def canberraDistance(x,y):
    return dist.chebyshev(x,y)

def getNeighbors(trainingSet, testInstance, k):
    #training set is a matrix
    #test instance is an array
    #k is the number of nearest neighbors to calculate

    distances = []
    # get the dimensions of the training set
    trainingSetRows = np.size(trainingSet, 0)
    trainingSetCols = np.size(trainingSet, 1)

    #for the test instance array
    testInstanceArray = testInstance
    #find the distance to each row in the training data
    for i in range(trainingSetRows):
        currentRow = []
        currentRowClass = 0
        for j in range(trainingSetCols - 1):
            currentRow.append(int(trainingSet.item(i, j)))
        currentRowClass = int(trainingSet.item(i, trainingSetCols - 1 ))
        similarity = euclideanDistance(currentRow, testInstance)
        # similarity = manhattanDistance(currentRow, testInstance)
        # similarity = cosineSimilarity(currentRow, testInstance)
        # similarity = chebyshevDistance(currentRow, testInstance)
        # similarity = canberraDistance(currentRow, testInstance)
        distances.append([similarity, currentRowClass])
    #sort the distances for each row in the training data
    distances.sort(key=operator.itemgetter(0))
    neighbors = []
    # print distances
    #return a list of the k closest classifications
    for i in range(k):
        neighbors.append(distances[i][1])

    #return classification of the test instance
    return neighbors

def neighborVote(neighbors):
    class1Count = neighbors.count(2)
    class2Count = neighbors.count(4)

    if class1Count > class2Count:
        # print "Voted as benign"
        return 2
    elif class1Count < class2Count:
        # print "Voted as Malignant"
        return 4
    elif class1Count == class2Count:
        print "there was a tie in the votes"
        return neighbors[0]

def classificationAccuracyA(classifications, actualClassifications):
    if not len(classifications) == len(actualClassifications):
        print "The lengths of the two arrays being compared for accuracy are not equal"
        return 0
    correctlyClassified = 0
    samples = len(classifications)
    for i in range(len(classifications)):
        if classifications[i] == actualClassifications[i]:
            correctlyClassified += 1
    accuracy = correctlyClassified / float(samples)
    return accuracy

def classificationAccuracyB(classifications, actualClassifications):
    if not len(classifications) == len(actualClassifications):
        print "The lengths of the two arrays being compared for accuracy are not equal"
        return 0

    class1Samples = actualClassifications.count(2)
    class2Samples = actualClassifications.count(4)
    correctClass1Count = 0
    correctClass2Count = 0

    for i in range(len(classifications)):
        if classifications[i] == actualClassifications[i]:
            if classifications[i] == 2:
                correctClass1Count += 1
            if classifications[i] == 4:
                correctClass2Count += 1

    # print correctClass1Count, correctClass2Count
    class1Acc = correctClass1Count / float(class1Samples)
    class2Acc = correctClass2Count / float(class2Samples)

    inner = class1Acc + class2Acc
    return inner*.5