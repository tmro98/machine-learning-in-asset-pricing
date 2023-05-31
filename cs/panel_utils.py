def scale_interact_sort(df, micro_cols, macro_cols):
    
    for date in df.index.unique():
        for feature in micro_cols:
            crosssec_min = df.loc[date, feature].values.min()
            crosssec_max = df.loc[date, feature].values.max()
            df.loc[date, feature] = df.loc[date, feature].apply(lambda x: (x - crosssec_min) / (crosssec_max - crosssec_min))
            
    for col in macro_cols:
        time_min = df[col].values.min()
        time_max = df[col].values.max()
        df[col] = df[col].apply(lambda x: (x - time_min) / (time_max - time_min))
    
    for col_macro in macro_cols:
        for col_micro in micro_cols:
            df[col_micro +"x"+ col_macro] = df[col_macro]*df[col_micro]
            
    return df.sort_index(inplace=True)