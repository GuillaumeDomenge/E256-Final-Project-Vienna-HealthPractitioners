import pandas as pd
from scipy import interpolate
import ast
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import *
import shapely
import math

with open('Data/Json/outputfile2', 'r') as f2:
    data = f2.read()

table = pd.read_csv("Data/CSV/doc_in_dist.csv")
df = pd.DataFrame(table)

districts = ["Alsergrund", "Brigittenau", "Döbling", "Donaustadt","Favoriten","Floridsdorf","Hernals","Hietzing","Innere Stadt","Josefstadt","Landstraße","Leopoldstadt","Liesing","Margareten","Mariahilf","Meidling","Neubau","Ottakring","Penzing","Rudolfsheim-Fünfhaus","Simmering","Währing","Wieden"]

def correct_coords(x):
    s = x["SHAPE"].strip("POINT)")[2:].split(" ")
    return float(s[0]),float(s[1])


naxs = []
nays = []
for i in range(len(df)):
    if df.iloc[i]["District"]=="NAN":
        v1,v2 = correct_coords(df.iloc[i])
        naxs.append(v1)
        nays.append(v2)


'''Opening geo data'''
data = ast.literal_eval(data)
l = []
for d in districts:
    l= l+ list(data[d])
#l = list(data["Alsergrund"])



'''Defining OG coordinates'''
xs = [item[1] for item in l]#OG x coordinates
ys = [item[0] for item in l]#OG y coordinates

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

'''getting poitns to plot interpolating function'''
print(naxs)
#iy = interp_func(ix)
#p = Polygon(l)
#c = shapely.centroid(p)
#print(c)
plt.scatter(naxs,nays,c="b")
plt.scatter(xs,ys,c="r")

#plt.plot(shapely.get_y(c),shapely.get_x(c),"o",c="k")
#print(p.covers(c))
#print(l)
#plt.scatter(ts,rs,c="r")
#plt.plot(ix,iy)
plt.show()
#print(l[1][0])     

#f_name = 'ARZTOGD.csv'
#df = pd.read_csv(f_name, delimiter=",")