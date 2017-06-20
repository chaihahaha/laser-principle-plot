import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import scipy.special as s

fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(-0.1, 0.1, 0.00025)
Y = np.arange(-0.1, 0.1, 0.00025)
X, Y = np.meshgrid(X, Y)
m = 9
n = 9
Amn = 1
E0 = 1
w0 = 0.01
wz = 0.03
# H=np.exp(X**2)(-30240*np.exp(-X**2)*X-512*np.exp(-X**2)*x**9+9216*np.exp(-X**2)*X**7-48384*np.exp(-X**2)*X**5+80640*np.exp(-X**2)*X**3)
u = np.sqrt(2) * X / wz
v = np.sqrt(2) * Y / wz
Z = (Amn * E0 * w0 * np.exp(u**2) * (-30240 * np.exp(-u**2) * u - 512 * np.exp(-u**2) * u**9 + 9216 * np.exp(-u**2) * u**7 - 48384 * np.exp(-u**2) * u**5 + 80640 * np.exp(-u**2) * u**3) * np.exp(v**2)
     * (-30240 * np.exp(-v**2) * v - 512 * np.exp(-v**2) * v**9 + 9216 * np.exp(-v**2) * v**7 - 48384 * np.exp(-v**2) * v**5 + 80640 * np.exp(-v**2) * v**3) * np.exp(-(X**2 + Y**2) / (wz**2)))**2

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.hot)
#ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=plt.cm.hot)
ax.set_zlim(0, 800000000000)

# savefig('../figures/plot3d_ex.png',dpi=48)
plt.show()
