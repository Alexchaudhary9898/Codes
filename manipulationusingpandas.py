import pandas as pd
import numpy as np
info_data = {'Name': ['john', 'scarlett', 'anna', 'emma', 'johnny', 'ash'],
        'age': ['10', '9','12', '11', '13', '14','8'],
        'grade': ['5', '4', '6', '6', '7', '8', '4'],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(info_data , index=labels)
print("Summary of the basic information about this Dataframe and its data:")
print(df.info())