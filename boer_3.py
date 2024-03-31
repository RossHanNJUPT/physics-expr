import matplotlib.pyplot as plt
import numpy as np
import sympy as sm

plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
t = sm.symbols('t')
theta = sm.symbols('theta',cls=sm.Function)

print("请输入阻尼系数：")
r = float(input())

print("请输入周期：")
T = float(input())
w = T/2*np.pi

w1 = 3

print("请输入驱动力大小：")
M = float(input())
A = M/(2*r*pow(pow(w1,2)-pow(r,2),0.5))

J = 250
theta_r = M/(J*pow(pow(pow(w1,2)-pow(w,2),2)+4*pow(r,2)*pow(w,2),0.5))
t = np.arange(0,10,0.01)
theta = A*np.cos(pow(pow(w,2)-pow(r,2),0.5)*t+np.pi/2)*np.exp(-r*t)+theta_r*np.cos(w*t+np.pi/2)
plt.plot(t,theta,"b*",label="受迫振动")
plt.grid()
plt.legend(loc="best")
plt.show()