import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.optimize import fsolve


xp10 = np.arange(-10,10,0.001)
def func(x):
    return (2-x**2+2*np.cos(5*np.arctan(1*x))+3*np.sin(5*np.arctan(1*x**2))) 
xs = []
ys = []
for x in xp10:
    def funcy(y):
        return y^2 -(2*np.cos(5*np.arctan(1*y))+3*np.sin(5*np.arctan(1*y**2)))-func(x)
    roots = fsolve(funcy,[-10,10])
    for root in roots:
        xs.append(x)
        ys.append(root)

# plt.plot(xp10,ys,"-",c="b")
# plt.plot(xp10,nys,"-",c="b")
# plt.plot(nxs,ys,"-",c="b")
# plt.plot(nxs,nys,"-",c="b")
plt.scatter(xs,ys,"o","r")
plt.show()

