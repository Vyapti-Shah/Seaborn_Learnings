import matplotlib.pyplot as plt
import seaborn as sns

a = sns.load_dataset("tips")
print(a)
sns.stripplot(x="day",y="total_bill",data=a)
plt.show()

sns.stripplot(x="day",y="total_bill",data=a,hue="sex",palette="rocket_r",
              linewidth=1,edgecolor="g",jitter=10, #jitter spreads the dots in plot
              size=5,marker="<",alpha=0.5)
plt.show()

#single strip plot
sns.stripplot(x=a["total_bill"])
plt.show()