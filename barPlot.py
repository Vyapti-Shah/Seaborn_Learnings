import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#commbined graph
a = sns.load_dataset("penguins")
print(a)
sns.barplot(x=a.island,y=a.bill_length_mm)
plt.show()

#separate graph
order_1 = ["Dream","Torgersen","Biscoe"]
sns.set_theme(style="darkgrid")
sns.barplot(x="island",y="bill_length_mm",data=a,hue="sex",#splits each bar into male and female
            order=order_1, #change the order of x-axis coordinates
            hue_order=["Female","Male"],ci=100, #changes the size above black line
            n_boot=2,orient="v",palette="icefire",saturation=1,errcolor="g",capsize=0.5,alpha=0.5)
plt.show()

#for making it horizontal 
sns.barplot(x="island",y="bill_length_mm",data=a,hue="sex",orient="h")
plt.show()
