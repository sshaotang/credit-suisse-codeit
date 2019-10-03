import logging
import json

from flask import request, jsonify;
import networkx as nx
from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/gun-control', methods=['POST'])
def guncontrol():
    data = request.get_json();
    print(data
    )
    return jsonify(fuelcontrol(data));



def fuelcontrol(input):

    grid = (input["grid"])
    fuel = input["fuel"]

    rows = len(grid)
    cols = len(grid[0])

    G=nx.DiGraph()
    pos = {}

    nodeCount = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "O":

                pos[nodeCount] = (i,j)
                nodeCount += 1

    for k,v in pos.items():
        for k2,v2 in pos.items():
                if (v[0]-1 <= v2[0] <= v[0]+1 and v[1] == v2[1]) or (v[1]-1 <= v2[1] <= v[1]+1 and v[0] == v2[0]):
                    G.add_edge(k,k2)



    paths = []
    pathslen = []

    for node in range(0,nodeCount):

#        print(list(G.neighbors(node)))
        if len(list(G.neighbors(node))) <= 2:
#            print(node, list(G.neighbors(node)))
            ls = list(nx.all_simple_paths(G,source=0,target=node))
#            print(ls)
#            print(len(ls[0]))
            if ls != []:
                paths.append(ls[0])
                pathslen.append(len(ls[0]))
                print()
#

    print(paths)
    print(pathslen)
    hm = {}


    for i in range(len(paths)):
        hm[pathslen[i]] = paths[i]


#    print(hm)

    pathslen.sort()

    hits = []

    for pl in pathslen:
#        print(pl)
        if fuel - pl >= 0:
            fuel -= pl
            c = pos[hm[pl][-1]]
            hits.append({"cell":{"x":c[1]+1,"y":c[0]+1}, "guns":pl})
        else:
            break
#

    return {"hits":hits}
