import numpy as np
import csv as csv
import pandas as pd
import sklearn as sklearn
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
import math

import Question2Plotting as Q2P

def poissonModel(lambdaVal, X):
    valueCount = len(X)
    productSummation = 0
    for i in range(valueCount):
        functionNumerator = math.exp(-lambdaVal*X[i])*(lambdaVal**X[i])
        functionDenom = math.factorial(X[i])
        functionValue = functionNumerator / functionDenom

        if i == 0:
            productSummation = functionValue
        else:
            productSummation = productSummation * functionValue
    return productSummation

def poissonEquation(x, valueArray):
    lambdaVal = arrayAverage(valueArray)
    functionNumerator = math.exp(-lambdaVal) * (lambdaVal ** x)
    functionDenom = math.factorial(x)
    functionValue = functionNumerator / functionDenom
    return functionValue

def arrayAverage(array):
    return sum(array)/len(array)
