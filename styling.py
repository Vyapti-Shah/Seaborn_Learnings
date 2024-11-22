import matplotlib.pyplot as plt
import seaborn as sns

#Seaborn Figure Styles
var = sns.load_dataset("tips")
print(var)
sns.boxplot(var["total_bill"])
plt.show()

sns.set_theme(style="darkgrid") #other: ticks for normal, whitegrid for light
sns.barplot(x="day",y="total_bill",data=var)
plt.grid()
plt.show()

#Removing Axes Spines
sns.set_theme(style="whitegrid")
sns.barplot(x="day",y="total_bill",data=var)
sns.despine() #removes the axis
plt.show()

#Scale and Context
sns.set_theme(style="whitegrid")
plt.figure(figsize=(12,3))
sns.set_context("poster",font_scale=2) #can also use poster,paper,talk
sns.barplot(x="day",y="total_bill",data=var,palette="cool")
sns.despine() #removes the axis
plt.show()