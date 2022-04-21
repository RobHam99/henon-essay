import numpy as np
import matplotlib.pyplot as plt

def separation(x1, y1, x2, y2):
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        

def lyapunov(delta_0, delta_n):
    return np.log(delta_n / delta_0)

def renorm(x1, y1, x2, y2, d1, d0):
    x2_r = x1 + d0 * (x2 - x1) / d1
    y2_r = y1 + d0 * (y2 - y1) / d1
    return x2_r, y2_r

def update(x_, y_, a_, b_):
    return 1 - a_ * x_**2 + y_, b_ * x_

b = 0.3
N = 10000
a = np.linspace(0., 2., 1000)
lya_arr = np.zeros(len(a))
for j in range(len(a)):
    d0 = 1E-12
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = d0
    lya = 0
    for i in range(N):
        x1_new, y1_new = update(x1, y1, a[j], b)
        x2_new, y2_new = update(x2, y2, a[j], b)
        d1 = separation(x1_new, y1_new, x2_new, y2_new)
        lya += (1 / (i + 1)) * lyapunov(d0, d1)
        x2, y2 = renorm(x1_new, y1_new, x2_new, y2_new, d1, d0)
        x1 = x1_new
        y2 = y2_new
    lya = lya / N
    lya_arr[j] = lya
    
plt.figure()
plt.plot(a, lya_arr)
plt.show()