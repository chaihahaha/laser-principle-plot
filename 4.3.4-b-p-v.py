import numpy as np
import matplotlib.pyplot as plt
vq = np.linspace(5 * 10**14, 7 * 10**14, 1000)
P = 15 * (10 * (np.exp(-4 * np.log(2) * ((vq - 6 * 10**14) / (1 * 10**14))**2) /
                (1 + np.sqrt(np.exp(-((vq - 6 * 10**14) / (0.03 * 10**14))**2) + 0.05)))**2 - 1)
plt.plot(vq, P)
plt.show()
