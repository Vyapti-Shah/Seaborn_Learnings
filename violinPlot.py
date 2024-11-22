import matplotlib.pyplot as plt
import seaborn as sns

a = sns.load_dataset("tips")
print(a)
sns.violinplot(x="day",y="total_bill",data=a)
plt.show()

sns.violinplot(x="day",y="total_bill",data=a,orient="h")
plt.show()

sns.violinplot(x="day",y="total_bill",data=a,hue="time",linewidth=2,palette="Dark2",saturation=0.6)
plt.show()

sns.violinplot(x="time",y="total_bill",data=a,order=["Dinner","Lunch"])
plt.show()

sns.violinplot(x="day",y="total_bill",data=a,hue="sex",split=True,scale="count")
plt.show()

sns.violinplot(x="day",y="total_bill",data=a,inner="point") #inner default is box #other types are quartile,stick
plt.show()

#single voilin plot
sns.violinplot(y=a["total_bill"]) #for maing it parallel to x axis use (x=a["total_bill"])
plt.show()
