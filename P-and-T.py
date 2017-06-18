import numpy as np 
import matplotlib.pyplot as plt 
T=np.linspace(0.01,0.99,100)
a=[0,0.005,0.01,0.07,0.1]
P=[0 for i in range(len(a))]
for j in range(len(a)):
    P[j]=2*T*(3/(a[j]-np.log(1-T))-1)/(2-T)
    plt.plot(T,P[j])
plt.show()