import matplotlib.pyplot as plt
import numpy as np


def dim_plot():
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlabel("dim")
    ax.set_ylabel("accuracy")
    plt.xlim(0, 350)
    plt.xticks(range(50, 350, 50))
    x = np.linspace(100,300,50)
    dim = [100, 150, 200, 250, 300]
    accuracy = [0.9043, 0.8738, 0.8642, 0.8622, 0.8458]
    ax.plot(dim, accuracy)
    plt.show()

def ac_lo_plot():
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlabel("epoch")
    ax.set_ylabel("accuracy")
    plt.xlim(0, 31)
    plt.xticks(range(0, 31, 3))
    x = np.linspace(1,30,30)
    accuracy = [0.6933, 0.7690, 0.8398, 0.8631, 0.8701, 0.8747, 0.8861, 0.8888, 0.8838, 0.8939, 0.8956, 0.8970, 0.8964,
                0.8984, 0.8984, 0.8955, 0.8990, 0.9001, 0.9007, 0.9025,0.8994,0.9026,0.9016,0.9036,0.9035,0.9038,0.9035,0.9046,0.9045,0.9043]
    loss = [0.5886,0.5289,0.4722,0.4530,0.4478,0.4438,0.4345,0.4236,0.4367,0.4286,0.4271,0.4262,0.4265,0.4249,0.4248,0.4270,0.4245,0.4235,0.4230,0.4216,0.4240,0.4216,0.4222,0.4206,0.4207,0.4205,0.4206,0.4198,0.4200,0.4201]
    ax.plot(x,accuracy)
    plt.show()

if __name__ == '__main__':
    dim_plot()