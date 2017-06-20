import numpy as np
import matplotlib.pyplot as plt
gl = np.linspace(0, 40, 1000)
dv = np.sqrt(gl / np.log((np.exp(gl) + 1) / 2) - 1)
plt.plot(gl, dv)
plt.show()
