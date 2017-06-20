import numpy as np
import matplotlib.pyplot as plt
l = np.linspace(0, 0.01, 1000)
k = 100
dk = 5
dv = 1
p20 = 1
p1 = dv * p20 * k**2 * \
    (np.sinh(np.sqrt(k**2 - dk**2 / 4) * l))**2 / (k**2 - dk**2 / 4)
p2 = p20 * (1 + k**2 * (np.sinh(np.sqrt(k**2 - dk**2 / 4) * l))
            ** 2 / (k**2 - dk**2 / 4))
plt.plot(l, p1)
plt.plot(l, p2)
plt.show()
