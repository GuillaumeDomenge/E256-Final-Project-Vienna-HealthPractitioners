import overpy
import folium
import simplejson as json
from pprint import pprint
import matplotlib.pyplot as plt
import itertools
from collections import OrderedDict
from tqdm import tqdm
import math

def distance(x,y):
    return 1000000*((x.lat-y.lat)**2+(x.lon-y.lon)**2)

def f7(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

def next_node(x,listx):
    try:
        minx = listx[0]
        for i in listx:
            if distance(x,i)<distance(x,minx):
                minx = i
        return minx
    except:
        return 0
    
def ringd(x):
    return sum([distance(x[i],x[(i+1)%len(x)]) for i in range(len(x))])

def get_relation_id_from_name(name):
    api = overpy.Overpass()
    result = api.query(f'rel[name="{name}"]; out;')
    if name=="Landstraße":
        return 1991416
    else:    
        if len(result.relations) > 0:
            return result.relations[0].id
        else:
            return None
        
def get_relation_id_from_name2(name):
    return d_dict[name]
    
def get_administrative_borders(relation_id):
    api = overpy.Overpass()
    result = api.query(f'relation({relation_id});(._;>;);out;')
    return result
# Function to print coordinates
def fill_coordinates(relation):
    dictini = relation.relations
    nodesdict = {}
    for node in relation.nodes:
        nodesdict[node.id] = (node.lat,node.lon)
    dictini2 = next(iter(dictini)).members
    dictways = {}
    for way in relation.ways:
        dictways[way.id] = way.nodes
    nodesl = []
    templ = []
    for relat in dictini2:
        print(relat.ref)
        templ = []
        try:
            a = [node.id  for node in dictways[relat.ref]]
            a.reverse()
            templ.append(a)
        except:
            a=2
            #templ.append([relat.ref])
        xs = [nodesdict[i][0] for i in templ[0]]
        ys = [nodesdict[i][1] for i in templ[0]]
        t = [i for i in range(len(xs))]
        plt.plot(xs,ys)
        plt.scatter(xs,ys,c=t,cmap="viridis")
        for i in range(len(xs)):
            plt.text(xs[i],ys[i],str(i))
    templ.reverse()
    for i in templ:
        nodesl+=i
    #nodesl = f7(nodesl)
    
    plt.show()
    coords = [nodesdict[node] for node in nodesl]
    return coords

def fill_coords_membersandswitch(relation):
    '''Gnerate list of all the ways'''
    # dictnodes = {}
    # for node in relation.nodes:
    #     dictnodes[node.id] = node
    membersl = relation.relations
    membersl = next(iter(membersl)).members
    dictways = {}
    dictwaystart = {}
    dictwaysend = {}
    for way in relation.ways:
        dictways[way.id] = way

    start_node = dictways[membersl[0].ref].nodes[0]
    nodesl = []

    for memb in membersl:
        try:
            way = dictways[memb.ref]
            if len(nodesl) == 0:
                nodesl += way.nodes
            else:
                if nodesl[-1] == way.nodes[0]:
                    nodesl += way.nodes
                else:
                    if nodesl[-1] == way.nodes[-1]:
                        a = way.nodes
                        a.reverse()
                        nodesl += a
                    else:
                        nodesl.reverse()
                        if nodesl[-1] == way.nodes[0]:
                            nodesl += way.nodes
                        else:
                            a = way.nodes
                            a.reverse()
                            nodesl += a
        except:
            print("error: bad ref")
    # xs = [node.lat for node in nodesl]
    # ys = [node.lon for node in nodesl]
    # t = [i for i in range(len(xs))]
    # plt.plot(xs,ys)
    # plt.scatter(xs,ys,c=t,cmap="viridis")
    # for i in range(len(xs)):
    #     plt.text(xs[i],ys[i],str(i))
    # plt.show()
    coords = [(node.lat,node.lon) for node in nodesl]

    return coords

def fill_coords_maybe_switch(relation):
    '''Gnerate list of all the ways'''
    # dictnodes = {}
    # for node in relation.nodes:
    #     dictnodes[node.id] = node
    membersl = relation.relations
    membersl = next(iter(membersl)).members
    waysl = []
    dictways = {}
    dictwaystart = {}
    dictwaysend = {}
    for way in relation.ways:
        waysl.append(way)
        dictways[way.nodes[0]] = way
        a = way.nodes
        dictwaystart[way.nodes[0]] = a
        dictwaysend[way.nodes[-1]] = a
        start_node = a[0]
    nodesl = []
    nodesl.append(start_node)
    nodesl += dictwaystart[start_node]
    waysl.remove(dictways[start_node])
    for way in waysl:
        a = way.nodes
        dictwaystart[way.nodes[0]] = a
        dictwaysend[way.nodes[-1]] = a
    current_node = nodesl[-1]
    print(current_node.id == start_node.id)

    while current_node.id != start_node.id:
        try:
            nodesl += dictwaystart[current_node]
            print(current_node)
            print(dictwaystart[current_node])
        except:
            a = dictwaysend[current_node]
            a.reverse()
            nodesl += a
            print(current_node)
            print(a)
        waysl.remove(dictways[current_node])
        for way in waysl:
            a = way.nodes
            dictwaystart[way.nodes[0]] = a
            dictwaysend[way.nodes[-1]] = a
        current_node = nodesl[-1]
        xs = [node.lat for node in nodesl]
        ys = [node.lon for node in nodesl]
        t = [i for i in range(len(xs))]
        plt.plot(xs,ys)
        plt.scatter(xs,ys,c=t,cmap="viridis")
        for i in range(len(xs)):
            plt.text(xs[i],ys[i],str(i))
        plt.show()
        
    coords = [(node.lat,node.lon) for node in nodesl]  
    

    return coords
    
    

def fill_coordinates_by_nodes(nodes):
    coords = []
    for node in admin_borders.nodes:
        coords.append((node.lat, node.lon))
    return coords

def draw_coordinates_on_map(district_name, coordinates):
    # Create a map centered on the first coordinate
    m = folium.Map(location=coordinates[0], zoom_start=10)

    # Add markers for each coordinate
    for coord in coordinates:
        folium.Marker(location=coord).add_to(m)

    # Save the map to an HTML file
    m.save('{}.html'.format(district_name))

#districts = ["Landstraße"]
d_dict = {"Alsergrund":1990590, "Brigittenau":1991433, "Döbling":1991435, "Donaustadt":1991434,"Favoriten":1991436,"Floridsdorf":1991437,"Hernals":1991438,"Hietzing":1990591,"Innere Stadt":1990592,"Josefstadt":1990593,"Landstraße":1991416,"Leopoldstadt":1990594,"Liesing":1991439,"Margareten":1991440,"Mariahilf":1990595,"Meidling":1990596,"Neubau":1990597,"Ottakring":1991441,"Penzing":1990598,"Rudolfsheim-Fünfhaus":1990599,"Simmering":1991442,"Währing":1990600,"Wieden":1991443}
districts = ["Alsergrund", "Brigittenau", "Döbling", "Donaustadt","Favoriten","Floridsdorf","Hernals","Hietzing","Innere Stadt","Josefstadt","Landstraße","Leopoldstadt","Liesing","Margareten","Mariahilf","Meidling","Neubau","Ottakring","Penzing","Rudolfsheim-Fünfhaus","Simmering","Währing","Wieden"]
coordinates_dictionary = {}

for d in districts:
    relation_id = get_relation_id_from_name2(d)
    print(d)
    if relation_id:
        admin_borders = get_administrative_borders(relation_id)
        coords = fill_coords_membersandswitch(admin_borders)
        coordinates_dictionary[d] = coords
        # print(type(coords))
        # print(coords)


with open('../Data/Json/outputfile_duo', 'w') as fout:
    json.dump(coordinates_dictionary, fout)


