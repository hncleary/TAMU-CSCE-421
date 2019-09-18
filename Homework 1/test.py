import numpy as np
print "Numpy Version: " , (np.__version__)

import csv as csv
print "CSV Version: " , (csv.__version__)

question1 = True

# load train csv
print "Loading Train CSV"
with open("hw1_question1_train.csv") as csvtrain:
    reader = csv.DictReader(csvtrain)
    test_table = [row.split(",") for row in csvtrain.read().replace("\r", "").split("\n")]
    # for row in reader:
    #     print row
    # print test_table

    test_table_matrix = np.matrix(test_table)
    # print test_table_matrix

    print test_table_matrix.item((0,9))
if not question1:
    #load dev csv
    print "Loading Dev CSV"
    with open("hw1_question2_dev.csv") as csvdev:
        reader = csv.DictReader(csvdev)
        for row in reader:
            print row

    #load test csv
    print "Loading Test CSV"
    with open("hw1_question2_test.csv") as csvtest:
        reader = csv.DictReader(csvtest)
        for row in reader:
            print row

# Question a.i
testMatrixRows = np.size(test_table_matrix,0)
testMatrixColumns = np.size(test_table_matrix,1)
# print testMatrixRows , testMatrixColumns
totalMalignant = 0
totalBenign = 0
for x in range(testMatrixRows):
    # print test_table_matrix.item(x, 9)
    # totalMalignant += 1
    if test_table_matrix.item(x,9) == "4":
        # print test_table_matrix.item(x,9)
        totalMalignant += 1
    elif test_table_matrix.item(x,9) == "2":
        totalBenign += 1
        # print "There is a serious issue with the csv data"
print "Malignant =",totalMalignant, "Benign =", totalBenign
totalPoints = totalMalignant + totalBenign
print "Total number of classified data points =", totalPoints

# Question a.ii
# plot the histogram of each feature
from matplotlib import pyplot as plt

#Attribute arrays
#1 clump thickness
clumpThickness = []
#2 uniformity of cell size
uniformityOfCellSize = []
#3 Uniformity of Cell Shape
uniformityOfCellShape = []
#4 Marginal Adhesion
marginalAdhesion = []
#5 Single Epithelial Size
singleEpithelialSize = []
#6 Bare Nuclei
bareNuclei = []
#7 bland chromatin
blandChromatin = []
#8 normal nucleoli
normalNucleoli = []
#9 mitoses
mitoses = []

#for each row
for i in range(testMatrixRows):
    #for each column in the row
    for j in range(testMatrixColumns - 1):
        currentValue = int(test_table_matrix.item(i,j))
        if j == 0:
            clumpThickness.append(currentValue)
        elif j == 1:
            uniformityOfCellSize.append(currentValue)
        elif j == 2:
            uniformityOfCellShape.append(currentValue)
        elif j == 3:
            marginalAdhesion.append(currentValue)
        elif j == 4:
            singleEpithelialSize.append(currentValue)
        elif j == 5:
            bareNuclei.append(currentValue)
        elif j == 6:
            blandChromatin.append(currentValue)
        elif j == 7:
            normalNucleoli.append(currentValue)
        elif j == 8:
            mitoses.append(currentValue)
        else:
            print "The scanner has gone oustide the column limit"

plotQuestion2 = False
if plotQuestion2:
    fig, ax = plt.subplots(3,3)
    fig.subplots_adjust(wspace = .3, hspace = .5)
    #1
    ax[0,0].hist(clumpThickness, [0,1,2,3,4,5,6,7,8,9,10] )
    ax[0,0].set_title('Clump Thickness')
    #2
    ax[0,1].hist(uniformityOfCellSize, [0,1,2,3,4,5,6,7,8,9,10] )
    ax[0,1].set_title('Uniformity of Cell Size')
    #3
    ax[0,2].hist(uniformityOfCellShape, [0,1,2,3,4,5,6,7,8,9,10] )
    ax[0,2].set_title('Uniformity of Cell Shape')
    #4
    ax[1,0].hist(marginalAdhesion, [0,1,2,3,4,5,6,7,8,9,10] )
    ax[1,0].set_title('Marginal Adhesion')
    #5
    ax[1,1].hist(singleEpithelialSize, [0,1,2,3,4,5,6,7,8,9,10] )
    ax[1,1].set_title('Single Epithelial Cell Size')
    #6
    ax[1,2].hist(bareNuclei, [0,1,2,3,4,5,6,7,8,9,10] )
    ax[1,2].set_title('Bare Nuclei')
    #7
    ax[2,0].hist(blandChromatin, [0,1,2,3,4,5,6,7,8,9,10] )
    ax[2,0].set_title('Bland Chromatin')
    #8
    ax[2,1].hist(normalNucleoli, [0,1,2,3,4,5,6,7,8,9,10] )
    ax[2,1].set_title('Normal Nuclei')
    #9
    ax[2,2].hist(mitoses, [0,1,2,3,4,5,6,7,8,9,10] )
    ax[2,2].set_title('Mitoses')


# Question a.iii plot scatter plots of 5 selected pairs
