import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Loading the datase
df=pd.read_csv(r'C:\Users\Dell\Desktop\data analysis\datasets\netflix.csv',encoding='latin1')
df.to_excel(r'C:\Users\Dell\Desktop\data analysis\datasets\netflix.xlsx',index=False)
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

#show status bar graph
status_count = df["Status"].value_counts()
plt.bar(status_count.index, status_count.values)
plt.title("Activity Status")
plt.xlabel("Activity")
plt.ylabel("Count")
plt.savefig('images/activity status')
plt.show()


#language bar graph 
language_count=df['Language'].value_counts()
plt.figure(figsize=(15,20))
plt.bar(language_count.index,language_count.values)
plt.title("language counts")
plt.savefig("images/language bar graph")
plt.show()


#piechart of table
table_counts=df['Table'].value_counts()
plt.pie(table_counts,labels=table_counts.index,autopct='%1.1f%%')
plt.title("Table comparision by percentage")
plt.savefig('images/TABLE piechart')
plt.show()

#seasonparsed
plt.hist(df["SeasonParsed"], bins=5)
plt.title("Distribution of Seasons")
plt.xlabel("Number of Seasons")
plt.ylabel("Count")
plt.show()
