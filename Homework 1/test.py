print "Numpy Version:"
import numpy as np
print (np.__version__)

print "CSV Version"
import csv as csv
print (csv.__version__)

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
        print test_table_matrix.item(x,9)
        totalMalignant += 1
    elif test_table_matrix.item(x,9) == "2":
        totalBenign += 1
        # print "There is a serious issue with the csv data"
print "Malignant =",totalMalignant, "Benign =", totalBenign
print "Total number of classified data points =", totalMalignant + totalBenign


# Question a.ii

