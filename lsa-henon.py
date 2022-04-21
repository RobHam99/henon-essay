import numpy as np
import matplotlib.pyplot as plt

a = np.linspace(0, 1.4, 100)
x_1 = (-0.7+np.sqrt(0.49+4*a))/2*a
lambda_1_1 = -a * x_1 + np.sqrt(a**2 * x_1**2 + 0.3)
lambda_1_2 = -a * x_1 - np.sqrt(a**2 * x_1**2 + 0.3)

x_2= (-0.7-np.sqrt(0.49+4*a))/2*a
lambda_2_1 = -a * x_2 + np.sqrt(a**2 * x_2**2 + 0.3)
lambda_2_2 = -a * x_2 - np.sqrt(a**2 * x_2**2 + 0.3)

plt.figure()
for i in range(len(a)):
    if abs(lambda_1_1[i]) < 1 and abs(lambda_1_2[i]) < 1:
        plt.plot(a[i], x_1[i], 'bx', markersize=3.5) # STABLE
    else:
        plt.plot(a[i], x_1[i], 'rx', markersize=3.5)
    if abs(lambda_2_1[i]) < 1 and abs(lambda_2_2[i]) < 1:
        plt.plot(a[i], x_2[i], 'bo', markersize=3.5) # STABLE
    else:
        plt.plot(a[i], x_2[i], 'ro', markersize=3.5)
plt.ylabel('x')
plt.xlabel('a')
plt.legend()
plt.show()

plt.figure()
plt.plot(a, lambda_1_1, label=r'$\lambda_1^1$')
plt.plot(a, lambda_1_2, label=r'$\lambda_1^2$')
plt.plot(a, lambda_2_1, label=r'$\lambda_2^1$')
plt.plot(a, lambda_2_2, label=r'$\lambda_2^2$')
plt.legend()
plt.show()