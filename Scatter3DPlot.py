from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

def main():
    iris=load_iris()
    X=iris.data
    Y=iris.target

    fig=plt.figure(figsize=(8,5))
    ax=fig.add_subplot(111,projection='3d')

    ax.scatter(X[:,2],X[:,3],X[:,0],c=Y,cmap="viridis",edgecolor='k')

    ax.set_xlabel("Petal Length")
    ax.set_ylabel("Petal Width")
    ax.set_zlabel("Sepal Length")

    plt.title("3D Visualization of Iris")
    plt.show()

if __name__ == "__main__":
    main()
