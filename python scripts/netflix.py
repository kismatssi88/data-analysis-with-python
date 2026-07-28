import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Loading the datase
df=pd.read_csv(r'C:\Users\Dell\Desktop\data analysis\datasets\netflix.csv',encoding='latin1')
print(df.head(5))
print(df.tail(5))
print(df.shape)
print(df.columns)


#dataset information 
print("the information of the daataset is")
print(df.info())

print("checking missing values")
print(df.isnull().sum())

#descriptive statistics
print(df.describe())

#activity bar graph
import matplotlib.pyplot as plt
acitivity=df['Active'].value_counts()
plt.figure()
plt.bar(acitivity.index,acitivity.values,colors=['red','blue'])
plt.title('show active or ended??')
plt.xlabel("ended or active")
plt.ylabel('counts')
plt.savefig("activity.png")
plt.show()
