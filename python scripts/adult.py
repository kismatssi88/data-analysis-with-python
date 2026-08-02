import pandas as pd
import matplotlib.pyplot as plt
#loading the data
df=pd.read_csv(r'C:\Users\Dell\Desktop\data analysis\datasets\adult.csv',encoding='latin1')
print(df.head(10))
print(df.tail(10))

#understanding the data
print(df.shape)
print(df.columns)
print(df.info())
print(df.isnull().sum())

#descriptive satistics
print(df.describe())

#sample dataset of 50 rows
sample=df.sample(n=50)
print(sample)

#cleaning the data /removing nan vlaues
df.isin(['?']).sum()


#makin