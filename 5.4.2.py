import numpy as np
import matplotlib.pyplot as plt
z = np.linspace(0, 0.6, 1000)
j0hv = [1000, 10**4, 2.5 * 10**4]
hvjz = [0 for i in range(len(j0hv))]
a = 5
z = 10 * z  # cm
dnhv = 2 * 10**6
for j in range(len(j0hv)):
    hvjz[j] = dnhv / (2 * a) + j0hv[j] * np.exp(-a * z) - \
        dnhv * np.exp(-a * z) / (2 * a)
    hvjz[j] = hvjz[j] / (10**4)  # J cm**-2
    plt.plot(z, hvjz[j])
plt.show()
