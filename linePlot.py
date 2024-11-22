import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#using dataframe from pandas
var = [1,2,3,4,5,6,7]
var_1 = [3,4,1,5,6,2,7]
x_1 = pd.DataFrame({"var":var,"var_1":var_1})
sns.lineplot(x="var",y="var_1",data=x_1)
plt.show()

#without using dataframe from pandas
var = [1,2,3,4,5,6,7]
var_1 = [3,4,1,5,6,2,7]
sns.lineplot(x=var,y=var_1)
plt.show()

#reading a data set
y_1 = sns.load_dataset("penguins").head(30) #head used when to work on a specific number of data only (here 30)
print(y_1)
sns.lineplot(x="bill_length_mm",y="flipper_length_mm",data=y_1,hue="sex",size=30,
             style="sex", #changes the style of sex into dotted
             palette="Accent", #changes the color
             markers=["o",">"],dashes=False,#removes the dotted line
             legend="full")
plt.grid()
plt.title("data set")
plt.show()
