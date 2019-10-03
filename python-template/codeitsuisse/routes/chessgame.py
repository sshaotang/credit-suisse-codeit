import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/chessgame', methods=['POST'])
def chessgame():
    data = request.get_json();

    return json.dumps(queen(data));



def queen(input_json):
    queen = 'K'
    obstacle = 'X'
    n = len(input_json)
    for i in range(n):
        for j in range(n):
            if input_json[i][j] == queen:
                queen_row = i
                queen_column = j

    positions = 0
    i = queen_row + 1
    while i < n:
        if input_json[i][queen_column] == obstacle:
            break
        positions += 1
        i += 1
    j = queen_row - 1
    while j > -1:
        if input_json[j][queen_column] == obstacle:
            break
        positions += 1
        j -= 1
    k = queen_column + 1
    while k < n:
        if input_json[queen_row][k] == obstacle:
            break
        positions += 1
        k += 1
    l = queen_column - 1
    while l > -1:
        if input_json[queen_row][l] == obstacle:
            break
        positions += 1
        l -= 1
    m = queen_row + 1
    o = queen_column + 1
    while m < n and o < n:
        if input_json[m][o] == obstacle:
            break
        positions += 1
        m += 1
        o += 1
    p = queen_row - 1
    q = queen_column - 1
    while p > -1 and q > -1:
        if input_json[p][q] == obstacle:
            break
        positions += 1
        p -= 1
        q -= 1
    r = queen_row + 1
    s = queen_column - 1
    while r < n and s > -1:
        if input_json[r][s] == obstacle:
            break
        positions += 1
        r += 1
        s -= 1
    t = queen_row - 1
    u = queen_column + 1
    while u < n and t > -1:
        if input_json[t][u] == obstacle:
            break
        positions += 1
        u += 1
        t -= 1
    return positions
