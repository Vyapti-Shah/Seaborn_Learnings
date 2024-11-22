import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

var = sns.load_dataset("tips")
print(var)
sns.pairplot(var,hue="sex",markers=["*","o"]) #forms a pair plot for the numerical values
plt.show()

sns.pairplot(var,vars=["total_bill","tip"] #to show only some data 
             ,hue="sex",hue_order=["Female","Male"],palette="BuGn",
             y_vars=["total_bill","tip"], #shows the variable on y-axis
             kind="kde",diag_kind="hist")
plt.show()