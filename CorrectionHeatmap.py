import seaborn as sns
import matplotlib.pylab as plt
import pandas as pd
from sklearn.datasets import load_iris

iris=load_iris()
df=pd.DataFrame(iris.data,columns=iris.feature_names)
corr=df.corr()

plt.figure(figsize=(6,5))

sns.heatmap(corr,annot=True,cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()