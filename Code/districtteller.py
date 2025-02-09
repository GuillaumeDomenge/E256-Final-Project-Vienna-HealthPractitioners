import numpy as np
import ast
import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame
from shapely.geometry import *
import shapely
'''Defining district names'''
districts = ["Alsergrund", "Brigittenau", "Döbling", "Donaustadt","Favoriten","Floridsdorf","Hernals","Hietzing","Innere Stadt","Josefstadt","Landstraße","Leopoldstadt","Liesing","Margareten","Mariahilf","Meidling","Neubau","Ottakring","Penzing","Rudolfsheim-Fünfhaus","Simmering","Währing","Wieden"]

'''Opening geo data'''
with open('../Data/Json/FinalMarkers', 'r') as f2:
    data = f2.read()
data = ast.literal_eval(data)

'''Defining district polygons'''
pdistricts = []
for d in districts:
    pdistricts.append(Polygon(list(data[d])))

'''Opening praxis doctor data'''
table = pd.read_csv("../Data/CSV/ARZTOGD.csv")
df = pd.DataFrame(table)


'''Function that return which district a doctor is from'''
def which_district(x):
    print(x["SHAPE"])
    s = x["SHAPE"].strip("POINT)")[2:].split(" ")
    p=Point(float(s[1]),float(s[0]))
    count = 0
    result = []
    while len(result)==0:
        print(count)
        if count <len(pdistricts):
            if pdistricts[count].covers(p) or pdistricts[count].contains(p):
                result.append(districts[count])
        else:
            result.append("NAN")
        count+=1
    return result[0]


'''Applying the function'''
df["District"]=df.apply(which_district,axis=1)
df.to_csv("../Data/CSV/doc_in_dist.csv",index=False)



#print(which_district(df.iloc[1]))
