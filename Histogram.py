import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris 

def main():
    df=pd.read_csv("iris.csv")

    plt.figure(figsize=(8,5))
    plt.hist(df['sepal length (cm)'],bins=10,color="skyblue",edgecolor="black")

    plt.xlabel("Sepal Length")
    plt.ylabel("Frequency")
    plt.title("Histogram Sepal Length Distribution")

    plt.grid(alpha=0.3)
    plt.show()

if __name__ == "__main__":
    main()