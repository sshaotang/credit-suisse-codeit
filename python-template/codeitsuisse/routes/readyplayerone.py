import random
import logging
import json

from flask import request, jsonify

from codeitsuisse import app;

@app.route('/readyplayerone', methods=['POST'])
def readyplayerone():
    data = request.get_json();
    return jsonify(ready(data));


def ready(input_json):
    n = input_json["maxChoosableInteger"]
    t = input_json["desiredTotal"]
    if n >= t:
        return 1
    total = 0
    i = 1
    while total < t:
        if i <= n:
            total += i
        i += 1
    maxMoves = i
    p1winner = False
    res = -1
    j = 0
    while not p1winner:
        if j > n**n:
            break
        jar1 = [k for k in range(1,n+1)]
        jar2 = 0
        for i in range(maxMoves):
            pick = random.randint(0,len(jar1)-1)
            jar2 += jar1[pick]
            jar1.pop(pick)
            if jar2 >= t and i%2 == 0:
                if i+1 < res or res == -1:
                    res = i+1
                p1winner = True
                break
        j += 1
    return {"res":res}
