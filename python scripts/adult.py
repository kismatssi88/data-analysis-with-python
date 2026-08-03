import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as np
#loading the data
df=pd.read_csv(r'datasets\for adult\adult.csv',na_values='?')
print(df.head(10))
print(df.tail(10))

#understanding the data
print(df.shape)
print(df.columns)
print(df.info())


#descriptive satistics
print(df.describe())

#sample dataset of 50 rows
sample=df.sample(n=50)
print(sample)

#cleaning the data /removing nan vlaues

missing=df.isin(['?']).sum()
print(missing)

#null values 
print(df.isnull().sum())

#contains so many   nan values so removing them 
df.dropna(how='any',inplace=True)
print(df.shape)

#checking duplicate data and dropping them we get
dup=df.duplicated().any()
print('Are there any duplicated data?',dup)
#removing duplicated data  
df=df.drop_duplicates()
print(df.shape)
#making a piechart  of workclass
workclass_counts = df['workclass'].value_counts()
plt.figure(figsize=(20, 12))
plt.pie(workclass_counts, labels=workclass_counts.index, autopct='%1.1f%%')
plt.title('Distribution of Workclass')
plt.savefig('images/adult visualizations/workclass_distribution.png')
plt.tight_layout()
plt.show()


