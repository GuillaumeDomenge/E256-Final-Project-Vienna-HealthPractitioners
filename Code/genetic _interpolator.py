import pandas as pd
import ast
import numpy as np
import matplotlib.pyplot as plt
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.optimize import minimize
from pymoo.core.problem import Problem
import math

with open('outputfile2', 'r') as f2:
    data = f2.read()

'''Opening geo data'''
data = ast.literal_eval(data)
l = list(data["Alsergrund"])

'''Defining OG coordinates'''
xs = [item[1] for item in l]#OG x coordinates
ys = [item[0] for item in l]#OG y coordinates
print(len(xs))

'''Define function of the difference between a point and it's parametric aproximation, where p are the parameters of the parametric interpolation.
In the case of a genetic algorithm p will be the chromosome vector'''
def func(x,y,p):
    x = x-p[0]
    y = y-p[1]
    val = -(x)**2-(y)**2+p[2]+p[3]*np.cos(p[4]*np.arctan(p[5]*x))+p[6]*np.sin(p[7]*np.arctan(p[8]*x))# left hand side + radius + x part of parametric
    val+= p[9]*np.cos(p[10]*np.arctan(p[11]*y))+p[12]*np.sin(p[13]*np.arctan(p[14]*y))# y part of parametric
    return np.abs(val)
'''Define the lower bounds and upper bounds for the parameters'''
lower = [min(xs),min(ys),0]
upper = [max(xs),max(ys),((max(xs)-min(xs))**2+(max(ys)-min(ys))**2)**(0.5)]

while len(lower)<15:
    lower.append(0)
    upper.append(10)

'''Define the genetic algorithm class for this particular problem'''
class intermin(Problem):

    def __init__(self):
        super().__init__(n_var=15, n_obj=len(xs), n_eq_constr=0, xl=lower, xu=upper)

    def _evaluate(self, x, out, *args, **kwargs):
        l1 = []
        for i in range(len(xs)):
            l2=[]
            for j in x:
                l2.append(func(xs[i],ys[i],j))
            l1.append(l2)
        
        out["F"] = np.column_stack(l1)


algorithm = NSGA2(pop_size=100)


problem = intermin()

res = minimize(problem,
               algorithm,
               ('n_gen', 400),
               seed=1,
               verbose=False)

vecxs = res.X
vecys = res.F

#plt.scatter(xs,ys,c="r")
#plt.scatter(ts,rs,c="r")
#plt.show()

print(vecxs[0])
print(vecys[0])

#f_name = 'ARZTOGD.csv'
#df = pd.read_csv(f_name, delimiter=",")