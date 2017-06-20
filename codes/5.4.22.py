import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 100, 1000)
s21 = 10**-3
dnl = 3 * 10**3
j0 = 1
gp = np.exp(s21 * dnl) / (np.exp(s21 * dnl) -
                          (np.exp(s21 * dnl) - 1) * np.exp(-2 * s21 * j0 * t))
plt.plot(t, gp)
plt.show()
