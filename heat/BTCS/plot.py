import matplotlib.pyplot as plt
import numpy as np
data0 = np.genfromtxt('sol0.dat')
data1 = np.genfromtxt('sol40.dat')
data2 = np.genfromtxt('sol80.dat')
data3 = np.genfromtxt('sol160.dat')
x = np.linspace(-1,1,data0.shape[0])
plt.plot(x,data0,'r',label="t=0.0")
plt.plot(x,data1,'g',label="t=0.5")
plt.plot(x,data2,'b',label="t=1.0")
plt.plot(x,data3,'k',label="t=2.0")
plt.xlabel('x')
plt.ylabel('heat distribution at time t')
plt.legend()
plt.show()
