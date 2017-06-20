import numpy as np
import matplotlib.pyplot as plt
gl = np.linspace(0, 50, 1000)
dv = np.sqrt((np.log(gl) - np.log(np.log((np.exp(gl) + 1) / 2))) / (np.log(2)))
plt.plot(gl, dv)
plt.show()
