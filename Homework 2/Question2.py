import numpy as np
print "Numpy Version: " , (np.__version__)

import csv as csv
print "CSV Version: " , (csv.__version__)

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

print noiseTestCols, noiseTestRows
print noiseTrainCols, noiseTrainRows

# print noiseTrain_matrix.item(2,0)

# Question (i)
# Plotting Histograms
from matplotlib import pyplot as plt
from histogramPlot import histogramPlot

histogramPlot(noiseTrain_matrix, noiseTrainRows, noiseTrainCols)

