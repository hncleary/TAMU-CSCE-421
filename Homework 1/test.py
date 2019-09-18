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

    plt.show()

# Question a.iii plot scatter plots of 5 selected pairs
#random pairs 2,5 - 3,8 - 1,6 - 4,7 - 6,3

#PAIR NO.1 2 & 5
pairOneXBenign = []
pairOneYBenign = []
pairOneXMalignant = []
pairOneYMalignant = []

for i in range(testMatrixRows):
    if int(test_table_matrix.item(i,9)) == 4 :
        pairOneXMalignant.append( int(test_table_matrix.item(i,1)) )
        pairOneYMalignant.append( int(test_table_matrix.item(i,4)) )
    if int(test_table_matrix.item(i,9)) == 2 :
        pairOneXBenign.append(int(test_table_matrix.item(i,1)))
        pairOneYBenign.append(int(test_table_matrix.item(i,4)))

#PAIR NO.2 3 & 8
pairTwoXBenign = []
pairTwoYBenign = []
pairTwoXMalignant = []
pairTwoYMalignant = []

for i in range(testMatrixRows):
    if int(test_table_matrix.item(i,9)) == 4 :
        pairTwoXMalignant.append( int(test_table_matrix.item(i,2)) )
        pairTwoYMalignant.append( int(test_table_matrix.item(i,7)) )
    if int(test_table_matrix.item(i,9)) == 2 :
        pairTwoXBenign.append(int(test_table_matrix.item(i,2)))
        pairTwoYBenign.append(int(test_table_matrix.item(i,7)))

#PAIR NO.3 1 & 6
pairThreeXBenign = []
pairThreeYBenign = []
pairThreeXMalignant = []
pairThreeYMalignant = []

for i in range(testMatrixRows):
    if int(test_table_matrix.item(i,9)) == 4 :
        pairThreeXMalignant.append( int(test_table_matrix.item(i,0)) )
        pairThreeYMalignant.append( int(test_table_matrix.item(i,5)) )
    if int(test_table_matrix.item(i,9)) == 2 :
        pairThreeXBenign.append(int(test_table_matrix.item(i,0)))
        pairThreeYBenign.append(int(test_table_matrix.item(i,5)))

#PAIR NO.4 4 & 7
pairFourXBenign = []
pairFourYBenign = []
pairFourXMalignant = []
pairFourYMalignant = []

for i in range(testMatrixRows):
    if int(test_table_matrix.item(i,9)) == 4 :
        pairFourXMalignant.append( int(test_table_matrix.item(i,3)) )
        pairFourYMalignant.append( int(test_table_matrix.item(i,6)) )
    if int(test_table_matrix.item(i,9)) == 2 :
        pairFourXBenign.append(int(test_table_matrix.item(i,3)))
        pairFourYBenign.append(int(test_table_matrix.item(i,6)))

#PAIR No.5 6 & 3
pairFiveXBenign = []
pairFiveYBenign = []
pairFiveXMalignant = []
pairFiveYMalignant = []

for i in range(testMatrixRows):
    if int(test_table_matrix.item(i,9)) == 4 :
        pairFiveXMalignant.append( int(test_table_matrix.item(i,5)) )
        pairFiveYMalignant.append( int(test_table_matrix.item(i,2)) )
    if int(test_table_matrix.item(i,9)) == 2 :
        pairFiveXBenign.append(int(test_table_matrix.item(i,5)))
        pairFiveYBenign.append(int(test_table_matrix.item(i,2)))


plotQuestion3 = False
if plotQuestion3:
    fig2, ax = plt.subplots(1,5)
    fig2.subplots_adjust(wspace = .3, hspace = .5)
    #PAIR NO. 1 Plot 2v5
    ax[0].scatter(pairOneXMalignant, pairOneYMalignant, color="red", alpha = .5)
    ax[0].scatter(pairOneXBenign, pairOneYBenign, color="blue", alpha = .5)
    ax[0].set_title('Feat. 2 vs. Feat. 5')
    #PAIR NO. 2 Plot 3v8
    ax[1].scatter(pairTwoXMalignant, pairTwoYMalignant, color="red", alpha = .5)
    ax[1].scatter(pairTwoXBenign, pairTwoYBenign, color="blue", alpha = .5)
    ax[1].set_title('Feat. 3 vs. Feat. 8')
    #PAIR NO.3 Plot 1v6
    ax[2].scatter(pairThreeXMalignant, pairThreeYMalignant, color="red", alpha = .5)
    ax[2].scatter(pairThreeXBenign, pairThreeYBenign, color="blue", alpha = .5)
    ax[2].set_title('Feat. 1 vs. Feat. 6')
    #PAIR NO.4 Plot 4v7
    ax[3].scatter(pairFourXMalignant, pairFourYMalignant, color="red", alpha = .5)
    ax[3].scatter(pairFourXBenign, pairFourYBenign, color="blue", alpha = .5)
    ax[3].set_title('Feat. 4 vs. Feat. 7')
    #PAIR No.5 Plot 6v3
    ax[4].scatter(pairFiveXMalignant, pairFiveYMalignant, color="red", alpha = .5)
    ax[4].scatter(pairFiveXBenign, pairFiveYBenign, color="blue", alpha = .5)
    ax[4].set_title('Feat. 6 vs. Feat. 3')

    plt.show()

# Question B-I
# Implement a KNN nearest neighbor classifier
from functions import euclideanDistance

x = (5,6,7)
y = (8,9,9)

print euclideanDistance(x, y)

