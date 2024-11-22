import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

var = np.linspace(1,10,20).reshape(4,5) #4,5=20elements
sns.heatmap(var)
plt.show()

data = sns.load_dataset("anagrams")
print(data) #cannot form a heatmap for string 
x = data.drop(columns=["attnr"],axis=1).head(10) #axis=1 to delete column
print(x)
sns.heatmap(x,vmin=0,vmax=12, #to change the min and max value of extent
            cmap='PuOr', #cmap=a to check all the info related to cmap similarly we can use a in same way forknowing any other command also
            annot=True)
plt.show()



var1 = np.linspace(1,10,10).reshape(2,5) #2,5=10elements
print(var1)
y = {"fontsize":10,"color":"g"} #to change the size and color of the inside nums a0,.... and b0,....
ar = np.array([["a0","a1","a2","a3","a4"],["b0","b1","b2","b3","b4"]])
print(ar)
v = sns.heatmap(var1,vmin=0,vmax=10,cmap='PuOr',annot=ar,fmt="s",annot_kws=y,linecolor="w",
            linewidths=10)#linewidth used to create gaps between the heap boxes
            #cbar=False) #used to remove color bar #xticklabels=False and yticklabels=False to remove the x and ylabels
v.set(xlabel="python",ylabel="data")
sns.set_theme(font_scale=1)
plt.show()