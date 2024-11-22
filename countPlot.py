import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#count plot = plots the count of the number of records by a category
#bar plot = plots the value or metric for each category

#count plot #it gives a value
a = sns.load_dataset("tips")
print(a)
sns.countplot(x="sex",data=a,hue="smoker",palette="bwr",saturation=0.5)
plt.show()

#comparing with bar plot #it gives a mean value
sns.barplot(x="sex",y="size",data=a)
plt.show()