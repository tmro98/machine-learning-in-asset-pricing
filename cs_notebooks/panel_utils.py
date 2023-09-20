import numpy 
import pandas 
import datetime

micro_cols = [
        'PPO', 'PVO', 'MOM10d', 'MOM60d', 'RSI', 'SRSI', 'SO', 'TSI', 'UO',
       'WR', 'EMV', 'FI', 'MFI', 'NVI', 'BBW', 'DC', 'UI', 'AI', 'CCI', 'KST',
       'MACD', 'MI', 'STC', 'TRIX', 'VI', 'BETA60d', 'BETA20d', 'BETA20d^2',
       'CHBETA', 'VOLA20d', 'VOLA60d', 'CHVOLA', 'MAXRET', 'MINRET', 'CHMOM',
       'RETURN', 'EXCESS_RETURN', 'AVG_EXCESS_RETURN',
]

macro_cols = [
    'MRKTMOM10d', 'MRKTMOM40d', 'MRKTVOLA', 'MRKT', 'DIVYIELD',
       'EARNYIELD', 'PERATIO', 'T10Y2Y', 'TB6TB3', 'TB3', 'TB6', 'PRIMETB3',
       'FFTB3', 'SENT1d', 'SENTCUM', 'SENTMA', 'CPI', 'UNRATE', 'RF',
]

def scale_interact_sort(df, micro_cols, macro_cols, interact = False):
    
    for date in df.index.unique():
        for feature in micro_cols:
            crosssec_min = df.loc[date, feature].values.min()
            crosssec_max = df.loc[date, feature].values.max()
            df.loc[date, feature] = df.loc[date, feature].apply(lambda x: (x - crosssec_min) / (crosssec_max - crosssec_min))
            
    for col in macro_cols:
        time_min = df[col].values.min()
        time_max = df[col].values.max()
        df[col] = df[col].apply(lambda x: (x - time_min) / (time_max - time_min))
    
    if interact:
        for col_macro in macro_cols:
            for col_micro in micro_cols:
                df[col_micro +"x"+ col_macro] = df[col_macro]*df[col_micro]
            
    df.sort_index(inplace=True)
            
    return "Done."

def holdout_cv(X_train, n_test):
    end_year = pandas.to_datetime(X_train.index[-1]).year
    start_year = end_year - n_test + 1
    
    test_start_date = datetime.date(start_year,1,31).strftime(format="%Y-%m-%d")
    test_end_date = datetime.date(end_year,12,31).strftime(format="%Y-%m-%d")

    test_range = X_train.index.slice_locs(start=test_start_date, end=test_end_date)
    
    train_idx = numpy.array(list(range(0, test_range[0])), dtype=int)
    test_idx = numpy.array(list(range(test_range[0], test_range[1])), dtype=int)
    
    yield (train_idx, test_idx) 


def modOOSR2(y_true, y_pred):
    numerator = ((y_true - y_pred.squeeze()) ** 2).sum(axis=0, dtype=numpy.float64)
    denominator = (y_true**2).sum(axis=0, dtype=numpy.float64)
    return 1 - (numerator/denominator)

def OOSR2(y_true, y_pred, mean_pred):
    numerator = ((y_true - y_pred.squeeze()) ** 2).sum(axis=0, dtype=numpy.float64)
    denominator = ((y_true - mean_pred)**2).sum(axis=0, dtype=numpy.float64)
    return 1 - (numerator/denominator)