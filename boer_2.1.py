import matplotlib.pyplot as plt
import numpy as np
import sympy as sm

plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
t = sm.symbols('t')
theta =  sm.symbols("theta",cls=sm.Function)

print("请输入最大振幅：")
A = float(input())
print("请输入阻尼系数：")
r = float(input())
w0 = 3
w1 = 2
t = np.arange(0,10,0.01)

print('请输入模式：')
model = int(input())
if model == 1:
    theta = A*np.cos(pow(pow(w0,2)-pow(r,2),0.5)*t)*np.exp(-r*t)
elif model == 2:
    theta = np.exp(-w0*t)*(A+(w1+w0*A)*t)
elif model == 3:
    wc = pow(pow(r,2)-pow(w0,2),0.5)
    theta = (np.exp(wc*t)*(w1+(r+wc)*A)/(2*wc)+np.exp(-wc*t)*(w1+(r-wc)*A)/(2*wc))*np.exp(-r*t)
plt.plot(t,theta,"b*",label="Scipy val")
plt.grid()
plt.legend(loc="best")
plt.show()