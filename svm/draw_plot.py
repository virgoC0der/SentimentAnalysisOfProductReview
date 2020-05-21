import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlabel("dim")
    ax.set_ylabel("accuracy")
    plt.xlim(0, 350)
    plt.xticks(range(50, 350, 50))
    x = np.linspace(100,300,50)
    dim = [100, 150, 200, 250, 300]
    accuracy = [0.8149, 0.8138, 0.8098, 0.7996, 0.8045]
    ax.plot(dim, accuracy)
    plt.show()