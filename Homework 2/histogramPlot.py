from matplotlib import pyplot as plt


def histogramPlot(data_matrix, matrixRows, matrixCols):
    rows = matrixRows
    cols = matrixCols

    # Plot a Histogram for Each of the Attributes

    # Attribute Arrays
    # 1 Frequency (Hertz)
    frequency = []
    # 2 Angle of Attack (Degrees)
    angleOfAttack = []
    # 3 Chord Length (Meters)
    chordLength = []
    # 4 Free-Steam Velocity (meters / second)
    freeSteamVelocity = []
    # 5 Suction Side Displacement Thickness ( meters )
    suctionSideDisplacement = []
    # 6 Scaled Sound Pressure Level (decibels)
    scaledSoundPressureLevel = []

    # append feature values to proper arrays
    for i in range(rows):
        for j in range(cols):
            currentValue = float(data_matrix.item(i,j))
            if j == 0:
                frequency.append(currentValue)
            elif j == 1:
                angleOfAttack.append(currentValue)
            elif j == 2:
                chordLength.append(currentValue)
            elif j == 3:
                freeSteamVelocity.append(currentValue)
            elif j == 4:
                suctionSideDisplacement.append(currentValue)
            elif j == 5:
                scaledSoundPressureLevel.append(currentValue)
    histBuckets = [1,2,3,4]
    # plot histogram of individual feature values
    fig, ax = plt.subplots(2,3)
    # fig.subplots_adjust(wspace =.3, hspace = .5)
    #1
    ax[0,0].hist(frequency)
    ax[0,0].set_title('Frequency (Hz)')
    #2
    ax[0,1].hist(angleOfAttack)
    ax[0,1].set_title('Angle of Attack (Deg.)')
    #3
    ax[0,2].hist(chordLength)
    ax[0,2].set_title('Chord Length (m)')
    #4
    ax[1,0].hist(freeSteamVelocity)
    ax[1,0].set_title('Free Steam Velocity m/s')
    #5
    ax[1,1].hist(suctionSideDisplacement)
    ax[1,1].set_title('Suction Side Disp. Thickness (m)')
    #6
    ax[1,2].hist(scaledSoundPressureLevel)
    ax[1,2].set_title('Scaled Sound Pressure (Decibels)')
    plt.show()
