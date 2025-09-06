import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
df = pd.read_csv("USA_Housing.csv")
print("\n_____ first 5 rows _____")
print(df.head)
print("\n_____Statistical Summary_____")
print(df.describe())
                                                                               