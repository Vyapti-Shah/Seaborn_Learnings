import matplotlib.pyplot as plt
import seaborn as sns

a = sns.load_dataset("tips")
print(a)
sns.swarmplot(x="day",y="total_bill",data=a,hue="time",dodge=True)
plt.show()