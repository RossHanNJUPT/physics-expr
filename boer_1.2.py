import matplotlib.pyplot as plt
import numpy as np
import sympy as sm

plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
t = sm.symbols('t')
theta = sm.symbols('theta',cls=sm.Function)

print("请输入最大振幅：")
A = float(input())
w = 3
t = np.arange(0,5,0.01)
theta = A*np.sin(w*t)
plt.plot(t,theta,"b*",label="Scipy val")
plt.grid()
plt.legend(loc="best")
plt.show()