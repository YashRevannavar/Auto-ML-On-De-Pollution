import numpy as np

def lstmMultiSplit(df, n_past, n_future):
    """
    Split the data into training x and y sets.
    **Note: The 1st column of the df should be the label column and other columns should be features.**
    :param df: dataframe
    :param n_past: number of past days we want to use to predict the future
    :param n_future: number of days we want to look into the future based on the past days
    :return: trainX and trainX train sets
    """
    trainX = []
    trainY = []

    # n_future = 1   # Number of days we want to look into the future based on the past days.
    # n_past = 5
    
    for i in range(n_past, len(df) - n_future +1):
        trainX.append(df[i - n_past:i, 0:df.shape[1]])
        trainY.append(df[i + n_future - 1:i + n_future, 0])
    trainX, trainY = np.array(trainX), np.array(trainY)
    return trainX, trainY

print("functionsAll.py loaded successfully")