import pandas as pd
from scipy import interpolate
import ast
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import *
import shapely
import math

with open('Data/Json/FinalMarkers', 'r') as f2:
    data = f2.read()


districts = ["Alsergrund", "Brigittenau", "Döbling", "Donaustadt","Favoriten","Floridsdorf","Hernals","Hietzing","Innere Stadt","Josefstadt","Landstraße","Leopoldstadt","Liesing","Margareten","Mariahilf","Meidling","Neubau","Ottakring","Penzing","Rudolfsheim-Fünfhaus","Simmering","Währing","Wieden"]

'''Opening geo data'''
data = ast.literal_eval(data)
l = []
for d in districts:
    l= l+ list(data[d])
l = list(data[districts[-1]])

'''Defining OG coordinates'''
xs = [item[1] for item in l[:-5]]#OG x coordinates
ys = [item[0] for item in l[:-5]]#OG y coordinates

'''Calculating marker centroid'''
cx = sum(xs)/len(xs)# Centroid x coordinate
cy = sum(ys)/len(ys)# Centroid y coordinate

'''Recentering markers'''
sxs = [x-cx for x in xs]# Shifted x coordinates
sys = [y-cy for y in ys]# Shifted y coordinates

'''Calculating polar coordinates of markers with respect to centroid'''
rs = [math.hypot(sxs[i],sys[i]) for i in range(len(xs)) ]# radius
ts = [math.atan2(sxs[i],sys[i]) for i in range(len(xs))]# theta

'''interpolating points'''
interp_func = interpolate.interp1d(ts,rs)


#p = Polygon(l)
#c = shapely.centroid(p)
#print(c)
t = [i for i in range(len(xs))]
plt.plot(xs,ys)
plt.scatter(xs,ys,c=t,cmap="viridis")
#plt.plot(16.319442488480775,48.23218871009019,"o",c="b")
#plt.plot(shapely.get_y(c),shapely.get_x(c),"o",c="k")
#print(p.covers(c))
#print(l)
#plt.scatter(ts,rs,c="r")
#plt.plot(ix,iy)
plt.show()
#print(l[1][0])

#f_name = 'ARZTOGD.csv'
#df = pd.read_csv(f_name, delimiter=",")