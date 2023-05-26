import numpy as np

def modOOSR2(y_true, y_pred):
    numerator = ((y_true - y_pred) ** 2).sum(axis=0, dtype=np.float64)
    denominator = (y_true**2).sum(axis=0, dtype=np.float64)
    return 1 - (numerator/denominator)

def OOSR2(y_true, y_pred, mean_pred):
    numerator = ((y_true - y_pred) ** 2).sum(axis=0, dtype=np.float64)
    denominator = ((y_true - mean_pred)**2).sum(axis=0, dtype=np.float64)
    return 1 - (numerator/denominator)