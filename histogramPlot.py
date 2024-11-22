import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

a =  sns.load_dataset("penguins")
print(a)
sns.displot(a["flipper_length_mm"],bins=[170,180,190,200,210,220,230,240],kde=True,#kernal density estimater
            rug=True,color="g") #log_scale=True)
plt.show()