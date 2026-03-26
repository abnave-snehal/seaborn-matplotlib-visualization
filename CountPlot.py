import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris

iris=load_iris()
df=pd.DataFrame(iris.data,columns=iris.feature_names)

df['variety']=iris.target
df['variety']=df['variety'].map({
    0:'Setosa',
    1:'Versicolor',
    2:'Verginica'
})

sns.countplot(x="variety",data=df)
plt.title("Count of each variety")
plt.show()