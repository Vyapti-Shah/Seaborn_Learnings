import matplotlib.pyplot as plt
import seaborn as sns

var = sns.load_dataset("tips").head(20)
print(var)
#as factor plot has now updated to catplot so now for using operations of factorplot we will have to use catplot command
#sns.factorplot(x="size",y="",data=var)
sns.catplot(x="tip",y="size",data=var,hue="sex",palette="BuPu",height=4) #height of the graph
plt.show()

sns.catplot(x="day",y="size",data=var,hue="sex",palette="Oranges",kind="bar") #kind helps us to decide which plot we want to use
plt.show()
sns.catplot(x="day",y="size",data=var,hue="sex",palette="Oranges",kind="box")
plt.show()
sns.catplot(x="day",y="size",data=var,hue="sex",palette="Oranges",kind="boxen")
plt.show()

#Categorical scatterplots with catplot -stripplot() => with kind="strip"
#                                      -swarmplot() => with kind="swarm"
#Categorical distribution plots with catplot - boxplot() => with kind="box"
#                                            - violinplot() => with kind="violin"
#                                            - boxenplot() => with kind="boxen"
#Categorical estimate plots with catplot - pointplot() => with kind="point"
#                                        - barplot() => with kind="bar"
#                                        - countplot() => with kind="count"