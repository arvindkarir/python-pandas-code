''' Panda tutorial
https://www.analyticsvidhya.com/blog/2016/01/complete-tutorial-learn-data-science-python-scratch-2/
'''


import pandas as pd
import csv
import numpy as np
import matplotlib as plt

df = pd.read_csv('C:\\Users\\User\Desktop\MIT EdX programming course\Py exercises\data_dump\Training.csv') #Reading the dataset in a dataframe using Pandas
df.head(10) # on cmd prompt prints first 10 rows of dataset
df.describe() # on cmd prompt prints count, mean, std, min, percentile etc

df['Property_Area'].value_counts() # indexing method for a particular column

df['ApplicantIncome'].hist(bins=50) # prints histogram
