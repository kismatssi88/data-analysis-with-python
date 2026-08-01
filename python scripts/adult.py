import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r'C:\Users\Dell\Desktop\data analysis\datasets\adult.csv',encoding='latin1')
print(df.head(5))
print(df.tail(5))
print(df.shape)
print(df.columns)
print(df.info())
print(df.isnull().sum())

#making bar graph of workclass
workclass_counts = df['workclass'].value_counts()
plt.bar(workclass_counts.index, workclass_counts.values)
plt.title("Workclass Counts")
plt.xlabel("Workclass")
plt.ylabel("Count")
plt.show()