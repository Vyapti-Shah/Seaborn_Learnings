import matplotlib.pyplot as plt
import seaborn as sns

var = sns.load_dataset("tips")
sns.set(style="whitegrid")
sns.boxplot(x="day",y="total_bill",data=var,palette="plasma",showmeans=True)
plt.show()

sns.boxplot(x="day",y="total_bill",data=var,hue="sex",color="g",order=["Fri","Sun","Thur","Sat"],
            showmeans=True,meanprops={"marker":"o","markeredgecolor":"b"},linewidth=3)
plt.show()

sns.boxplot(y="day",x="total_bill",data=var,hue="sex") #to make it horizontal interchange the x and y axis variables
plt.show()

sns.boxplot(data=var,showmeans=True,meanprops={"marker":"o","markeredgecolor":"b"},linewidth=3,palette="plasma",orient="h")
plt.show()

#single box plot
sns.boxplot(var["total_bill"])
plt.show()
