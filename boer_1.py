import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as s

plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
def dfunc(theta,t):
    u,v=theta
    k = 500
    J = 250
    return np.array([v,-k*u/J])
t = np.arange(0,30,0.1)
ans1 = s.odeint(dfunc,[0.0,1.0],t)

plt.plot(t,ans1[:,0],"b*",label="Scipy val")
plt.grid()
plt.legend(loc="best")
plt.show()