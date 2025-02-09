import ast
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import *
import simplejson as json
from tqdm import tqdm
import math
from python_tsp.exact import solve_tsp_dynamic_programming, solve_tsp_brute_force, solve_tsp_branch_and_bound
from python_tsp.heuristics import solve_tsp_local_search
from py2opt.routefinder import RouteFinder

with open('../Data/Json/outputfile2', 'r') as f2:
    data = f2.read()


districts = ["Alsergrund", "Brigittenau", "Döbling", "Donaustadt","Favoriten","Floridsdorf","Hernals","Hietzing","Innere Stadt","Josefstadt","Landstraße","Leopoldstadt","Liesing","Margareten","Mariahilf","Meidling","Neubau","Ottakring","Penzing","Rudolfsheim-Fünfhaus","Simmering","Währing","Wieden"]

'''Opening geo data'''
data = ast.literal_eval(data)
l = []
newdata = {}

def distance(x1,x2):
    return ((x1[0]-x2[0])**2+(x1[1]-x2[1])**2)**(0.5)

def ringd(l1):
    val = sum([distance(l1[i],l1[(i+1)%len(l1)]) for i in range(len(l1))])
    return val

def returnuniquelist(x):
    temp = []
    for i in range(len(x)):
        if x[i] not in temp:
            temp.append(x[i])
    return temp


'''Organize with closest'''
# with tqdm(total=23) as p_bar:
#     for d in districts:
#         l= list(data[d])
#         dists = np.array([[distance(l[i],l[j]) for i in range(len(l))] for j in range(len(l))])
#         sol , bined = solve_tsp_branch_and_bound(dists)
#         l2 = [l[i] for i in sol]
#         newdata[d]=l2
#         p_bar.update(1)


with tqdm(total=23) as p_bar:
    for d in districts:
        l= list(data[d])
        l = returnuniquelist(l)
        dists = [[1000000*distance(l[i],l[j]) for i in range(len(l))] for j in range(len(l))]
        route_finder = RouteFinder(dists, [i for i in range(len(l))], iterations = 5, return_to_begin=True)
        best_distance, best_route = route_finder.solve()
        l2 = [l[i] for i in best_route]
        newdata[d]=l2
        p_bar.update(1)



'''Organize by shifting furthest'''
# l=newdata
# with tqdm(total=23) as p_bar:
#     for d in districts:
#         l= list(data[d])
#         out = 0
#         while out==0:
#             l2 = [distance(l[i],l[(i-1)%len(l)])+distance(l[i],l[(i+1)%len(l)]) for i in range(len(l))]
#             index_max = max(range(len(l2)),key=l2.__getitem__)
#             out2 = 0
#             l3 = l
#             count = 0
#             for i in range(len(l)):
#                 holdm = l3.pop(index_max)
#                 l3.insert(i,holdm)
#                 index_max = i
#                 if ringd(l3)<ringd(l):
#                     l=l3
#                     print("changed")
#                 else:
#                     count+=1
#             if count== len(l):
#                 out2=1
#             out=out2
#         newdata[d]=l
#         p_bar.update(1)

with open('../Data/Json/OrderedMarkers', 'w') as fout:
    json.dump(newdata, fout)

