import numpy as np
import matplotlib.pyplot as plt

def update_coords(x, y, alpha = 1.4, beta = 0.3):
    return 1 - alpha * x**2 + y, beta * x


if __name__ == '__main__':
    iter = 100000
    a = 1.4
    b = 0.3
    trajectory_1 = np.zeros((iter + 1, 2))
    #trajectory_2 = np.zeros((iter + 1, 2))
    trajectory_1[0] = np.array([0.0, 0.0])
    #trajectory_2[0] = np.array([0.02, 0.02])
    for i in range(iter):
        trajectory_1[i+1] = update_coords(trajectory_1[i][0], trajectory_1[i][1], a, b)
        #trajectory_2[i+1] = update_coords(trajectory_2[i][0], trajectory_2[i][1], a, b)

    t = np.linspace(0, iter+1, iter + 1)
    plt.figure()
    plt.plot(trajectory_1[:, 0], trajectory_1[:, 1], 'ko', markersize=1.5)#, label='Trajectory 1: $x_0, y_0 = 0.01, 0.01$')
    #plt.plot(trajectory_2[:, 0], trajectory_2[:, 1], 'ro', markersize=2.5, label='Trajectory 2: $x_0, y_0 = 0.02, 0.02$')
    #plt.plot(trajectory_1[-1, 0], trajectory_1[-1, 1], 'ko', markersize=8, label='Trajectory 1: final point')
    #plt.plot(trajectory_2[-1, 0], trajectory_2[-1, 1], 'ro', markersize=8, label='Trajectory 2: final point')
    plt.xlabel('x')
    plt.ylabel('y')
    #plt.legend()
    plt.show()

    plt.figure()
    plt.plot(t[-50:], trajectory_1[-50:, 0])
    plt.xlabel('t')
    plt.ylabel('x')
    plt.show()

    plt.figure()
    plt.plot(t[-50:], trajectory_1[-50:, 1])
    plt.xlabel('t')
    plt.ylabel('y')
    plt.show()

