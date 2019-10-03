import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/wedding-nightmare', methods=['POST'])
def weddingnightmare():
    data = request.get_json()
    return json.dumps(wedding_nightmare(data));

def wedding_nightmare(array):
    output = []
    for a in array:
        test_case = a['test_case']
        friends = a['friends']
        enemies = a['enemies']
        families = a['families']
        tables = a['tables']
        guests = a['guests']
        satisfiable = True
        allocation = [[] for i in range(tables)]
        # allocated = [False for i in range(guests)]
        # for i in range(len(friends)):
        #     for j in friends[i]:
        #         if not allocated[j-1]:
        #             allocation[i].append(j)
        #             allocated[j-1] = True
        #             friends[i].remove(j)
        #     if friends[i] != []:
        allocation[0] = [i+1 for i in range(guests)]
        i = 0
        try:
            while True:
                if i == tables:
                    break
                if enemies != []:
                    # enemies = sorted(enemies, key = lambda x: x[0])
                    for e in enemies:
                        e = sorted(e)
                        if e[0] in allocation[i] and e[1] in allocation[i]:
                            allocation[i].remove(e[0])
                            allocation[i+1].append(e[0])
                if friends != []:
                    friends = sorted(friends, key = lambda x: x[0])
                    for fr in friends:
                        fr = sorted(fr)
                        if fr[0] in allocation[i] and fr[1] in allocation[i]:
                            pass
                        elif fr[0] in allocation[i] and fr[1] not in allocation[i]:
                            allocation[i].remove(fr[0])
                            allocation[i+1].append(fr[0])
                        elif fr[0] not in allocation[i] and fr[1] in allocation[i]:
                            allocation[i].remove(fr[1])
                            allocation[i+1].append(fr[1])
                if families != []:
                    families = sorted(families, key = lambda x: x[0])
                    for fa in families:
                        fa = set(sorted(fa))
                        if fa.issubset(set(allocation[i])):
                            pass
                        else:
                            for member in fa:
                                if member in allocation[i]:
                                    allocation[i].remove(member)
                                    allocation[i+1].append(member)
                i += 1
        except IndexError:
            satisfiable = False
        allocation_formatted = []
        for i in range(len(allocation)):
            for j in allocation[i]:
                allocation_formatted.append([j,i+1])
        if satisfiable:
            output.append({'test_case':test_case, 'satisfiable':satisfiable, 'allocation':allocation_formatted})
        else:
            output.append({'test_case':test_case, 'satisfiable':satisfiable,'allocation':[]})
    return output
