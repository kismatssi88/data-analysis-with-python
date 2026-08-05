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

#removing cloumns which give same things like educational-num,capital-loss,capital-gain
df=df.drop(['educational-num','capital-gain','capital-loss'],axis=1)
print(df.shape)

#univariate analysis i.e .analysis of a single column

#distrubution of age  column where we will find the descriptive statstics and make  a histogram
df['age'].describe()
df['age'].hist()
plt.savefig(r'C:\Users\Dell\Desktop\data analysis\images\adult visualizations\adult age.png')

#no. of person aged between 17 to 48 here we can use between()
total=sum(df['age'].between(17,48))
print(total)



#distrubution of workclass column
df['workclass'].describe()
df['age'].hist()
plt.savefig(r'C:\Users\Dell\Desktop\data analysis\images\adult visualizations\adult workclass.png')

#number of person doing bachelors & master
total=sum(df['education'].between('Bachelors','Masters'))
print(total)

#workclass which get the highest salary

values=df['income'].unique()
print(values)
count=df['income'].value_counts()
print(count)
