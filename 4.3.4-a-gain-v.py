import numpy as np
import matplotlib.pyplot as plt
vq = np.linspace(5 * 10**14, 7 * 10**14, 1000)
g = 10 * np.exp(-4 * np.log(2) * ((vq - 6 * 10**14) / (1 * 10**14))**2) / (55 * np.sqrt(4 * np.exp(-((vq - 6 * 10**14) / (0.03 * 10**14))**2) + 0.05 +
                                                                                        np.exp(-((vq - 5.5 * 10**14) / (0.03 * 10**14))**2) + np.exp(-((vq - 6.5 * 10**14) / (0.03 * 10**14))**2)))
g0 = 0.82 * np.exp(-4 * np.log(2) * ((vq - 6 * 10**14) / (1 * 10**14))**2)
plt.plot(vq, g)
plt.plot(vq, g0)
gt = [0.086 for i in vq]
plt.plot(vq, gt)
plt.show()
