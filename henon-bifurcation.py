import matplotlib.pyplot as plt
import numpy as np
from henon import update_coords

iter = 1000
b = 0.3
a = np.linspace(0., 1.4, 10000)
N = 50
final = np.zeros((len(a), N))
for j in range(len(a)):
    x_arr = np.zeros(N)
    x = 0
    y = 0
    c = 0
    for i in range(iter):
        x_new, y_new = update_coords(x, y, a[j], b)
        if i >= iter - N:
            x_arr[c] = x_new
            c += 1
        x = x_new
        y = y_new
    final[j] = x_arr

plt.figure()
plt.plot(a, final, 'ko', markersize=0.05)
plt.xlabel('a')
plt.ylabel('x')
plt.show()
