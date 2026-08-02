import pandas as pd
import matplotlib.pyplot as plt
#loading the data
df=pd.read_csv(r'datasets\for adult\adult.csv')
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


#making a piechart  of workclass
workclass_counts = df['workclass'].value_counts()
plt.figure(figsize=(20, 12))
plt.pie(workclass_counts, labels=workclass_counts.index, autopct='%1.1f%%')
plt.title('Distribution of Workclass')
plt.savefig('images/adult visualizations/workclass_distribution.png')
plt.show()

#making native country distributin by bar graph
import matplotlib.pyplot as plt

# Native country distribution
native_country_counts = df['native.country'].value_counts()

plt.figure(figsize=(20, 12))
plt.bar(native_country_counts.index, native_country_counts.values)

plt.title('Distribution of Native Country')
plt.xlabel('Native Country')
plt.ylabel('Count')

plt.xticks(rotation=90)      # Rotate country names
plt.tight_layout()           # Adjust layout

plt.savefig('images/adult visualizations/native_country_distribution.png')
plt.show()