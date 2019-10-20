import numpy as np
import csv as csv
import pandas as pd
import sklearn as sklearn
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime

def convertDateTime(date_time):


    date = date_time.split(" ")[0]
    time = date_time.split(" ")[1]
    day, month, year = date.split("-")
    day, month, year = int(day), int(month), int(year)
    hour = time.split(":")[0]
    hour = int(hour)
    # calculate number of hours elapsed since original time stamp
    dt = datetime(year, month, day, hour, 0, 0, 0)
    return dt.timestamp()

def dataTicketsSold(dataMatrix):
    data = dataMatrix
    rows = data.shape[0]
    cols = data.shape[0]

    beginDateTime = "25-08-2012 0:00"
    convertedBeginDateTime = convertDateTime(beginDateTime)
    X = []
    Y = []
    for i in range(rows):
        if i == 0:
            continue
        # append X values to input array
        currentValue = ( convertDateTime(data.iat[i, 0]) - convertedBeginDateTime ) / 3600
        X.append(currentValue)
        # append Y values to output array
        currentValue = float( data.iat[i, 1] )
        Y.append(currentValue)
    return X, Y

def dataTicketsSoldFirstMonth(dataMatrix):
    data = dataMatrix
    rows = data.shape[0]
    cols = data.shape[0]

    beginDateTime = "25-08-2012 0:00"
    convertedBeginDateTime = convertDateTime(beginDateTime)
    X = []
    Y = []
    for i in range(744):
        if i == 0:
            continue
        # append X values to input array
        currentValue = ( convertDateTime(data.iat[i, 0]) - convertedBeginDateTime ) / 3600
        X.append(currentValue)
        # append Y values to output array
        currentValue = float( data.iat[i, 1] )
        Y.append(currentValue)
    return X, Y

def plotValues(X, Y):
    plt.plot(X, Y)
    plt.ylabel("Tickets Sold")
    plt.xlabel("Hours Elapsed Since August 25, 2012")
    plt.show()
    return 0


