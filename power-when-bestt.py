import numpy as np
import matplotlib.pyplot as plt
gml2=np.linspace(0,10,1000)
a=[0.1,0.05,0.01,0.005]
Tm=[0 for i in range(4)]
for j in range(4):
    Tm[j]=np.sqrt(gml2*a[j])-a[j]
    plt.plot(gml2,Tm[j])
plt.show()