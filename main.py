import pandas as pd
import numpy as np
import csv

with open('salaries_by_college_major.csv', 'r') as file:
    df = pd.DataFrame(file)
    
    data_dict = df.to_dict('list')
    
    # for key,value in data_dict.items():
    #     print(f'key:{key}, value:{value}\n')
    print(df)
    print(df.iloc[5])
    
    print(df.loc[0,2])