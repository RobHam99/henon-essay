import numpy as np
import matplotlib.pyplot as plt

def logr(r, x):
    return r * x * (1 - x)


N = 100

r = np.linspace(2., 4, 100)
lya = np.zeros(len(r))
for j in range(len(r)):
    x1_a = np.zeros(N+1)
    x1_a[0] = 0.1
    for i in range(N):
        x1_a[i+1] = logr(r[j], x1_a[i])
        lya[j] += 1/N * np.log(abs(r[j] - 2 * r[j] * x1_a[i]))
    
plt.figure()
plt.plot(r, lya)
plt.ylim([-1, 1])
plt.show()