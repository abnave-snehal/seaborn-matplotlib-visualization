import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

def main():
    iris=load_iris()

    df=pd.DataFrame(iris.data,columns=iris.feature_names)

    plt.figure(figsize=(8,5))

    plt.scatter(df['sepal length (cm)'],df['petal length (cm)'])
    plt.xlabel("Petal Length")
    plt.ylabel("Petal Width")

    plt.title("Scatter Plot: Sepal vs Petal Length")
    plt.show()

if __name__ == "__main__":
    main()
