import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    df=pd.read_csv("iris.csv")

    plt.figure(figsize=(8,5))
    sns.boxplot(x="species",y="petal length (cm)",data=df)

    plt.title("Boxplot Petal Length By Variety")
    plt.show()

if __name__ == "__main__":
    main()