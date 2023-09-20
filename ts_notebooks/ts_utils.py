import numpy as np

# for testing
def OOSR2(y_true, y_pred, mean_pred):
    numerator = ((y_true - y_pred.squeeze()) ** 2).sum(axis=0, dtype=np.float64)
    denominator = ((y_true - mean_pred)**2).sum(axis=0, dtype=np.float64)
    return 1 - (numerator/denominator)