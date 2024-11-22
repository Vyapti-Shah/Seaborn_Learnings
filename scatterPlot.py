import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

a = sns.load_dataset("penguins").head(20)
m = {"Male":"o","Female":"*"}
print(a)
sns.scatterplot(x="bill_length_mm",y="bill_depth_mm",data=a,hue="sex",style="sex",size="sex",
                sizes=(100,90),palette="gist_ncar",alpha=1,markers=m)
plt.show()