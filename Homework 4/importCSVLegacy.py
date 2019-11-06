import numpy as np
import csv as csv
import pandas as pd
import sklearn as sklearn
import seaborn as sns

print ("Numpy Version: " , (np.__version__))
print ("CSV Version: " , (csv.__version__))
print ("Pandas Version: " , (pd.__version__))
print ("Sci-Kit-Learn Version: " , (sklearn.__version__))
print ("Seaborn Version: " , (sns.__version__))

legacyImport = False

if legacyImport:
    with open("OnlineNewsPopularityTest.csv") as csvPopularityTest:
        reader = csv.DictReader(csvPopularityTest)
        popularityTest_table = [row.split(",") for row in csvPopularityTest.read().replace("\r", "").split("\n")]
        popularityTest_matrix = np.matrix(popularityTest_table)
    popularityTestRows = np.size(popularityTest_matrix, 0)
    popularityTestCols = np.size(popularityTest_matrix, 1)

    with open("OnlineNewsPopularityTrain.csv") as csvPopularityTrain:
        reader = csv.DictReader(csvPopularityTrain)
        popularityTrain_table = [row.split(",") for row in csvPopularityTrain.read().replace("\r", "").split("\n")]
        popularityTrain_matrix = np.matrix(popularityTrain_table)
    popularityTrainRows = np.size(popularityTest_matrix, 0)
    popularityTrainCols = np.size(popularityTest_matrix, 1)