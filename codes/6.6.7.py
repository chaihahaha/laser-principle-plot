import numpy as np
import matplotlib.pyplot as plt
gl = np.linspace(0, 10, 1000)
a = 1
ai = 5
p2 = ai * (np.sqrt(2 * gl) - np.sqrt(a))**2 / 2
p1 = ai * (np.sqrt(2 * gl / a) - a) / 2
plt.plot(gl, p2)
plt.plot(gl, p1)
plt.show()
