import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = sns.load_dataset("penguins")
print(df.shape)
print(df.head())
print(df.tail())
print(df.isnull().sum())
print(df.describe())
print(df.describe(include='all').T)
print(df.dtypes)
corr_matrix = df.select_dtypes(include='number').corr()
print(corr_matrix)
sns.heatmap(corr_matrix, cmap='Wistia', annot=True)
plt.show()
df.hist(figsize=(12, 8))
plt.show()