import numpy as np
import matplotlib.pyplot as plt
dvc = np.linspace(0, 100000, 1000)
dnt = [10, 50, 100, 150]
dvs = [0 for i in range(4)]
n2t = 10**(-3)
hv = 10**(-10)
p0 = 1
for j in range(4):
    dvs[j] = 2 * np.pi * n2t * dvc**2 * hv / (dnt[j] * p0)
    plt.plot(dvc, dvs[j])
plt.show()
