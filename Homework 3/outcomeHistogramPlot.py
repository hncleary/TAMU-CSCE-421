from matplotlib import pyplot as plt

def outcomeHistogramPlot(data_matrix, matrixRows, matrixCols):
    rows = matrixRows
    cols = matrixCols

    # "area" area burned is the outcome from column 13
    outcome = []

    for i in range(rows - 1):
        if i == 0:
            continue
        currentValue = float(data_matrix.item(i, matrixCols - 1))
        outcome.append(currentValue)

    fig, ax = plt.subplots(1 , 3)

    ax[0].hist(outcome, bins = [0, 10, 20, 30, 40, 50, 100, 200, 300] )
    ax[0].set_title('Outcome - Forest Area Burned')

    plt.show()

    print max(outcome)
    return 0