import logging
import json
import collections
import networkx as nx

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/generateSequence', methods=['POST'])
def genSeq():
    data = request.get_json()
    print(data)
    return jsonify(dependency(data));


def dependency(input):


    modules = input["modules"]
    pairs = input["dependencyPairs"]

    if modules == []:
        return []

    if pairs == []:
        return modules

    while True:

        G = nx.DiGraph()

        map(G.add_node, range(len(pairs)))

        for pair in pairs:
            if pair["dependentOn"] != pair["dependee"] and pair["dependentOn"] in modules and pair["dependee"] in modules:
                G.add_edge(pair["dependentOn"],pair["dependee"])

        pos=nx.spring_layout(G)

        # nx.draw(G,pos, edge_color='r')

        try:
            topo = list(nx.topological_sort(G))
            return topo

        except Exception as e:
            topo = list(nx.find_cycle(G, orientation='ignore'))

            for t in topo:
                modules.remove(t[0])

            if len(modules) <= 1:
                return modules
