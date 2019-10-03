import logging
import json

from flask import request, jsonify

from codeitsuisse import app


@app.route('/defuse', methods=['GET'])
def defuse():
    data = request.get_json();
    output = []

    for x in data:
        output.append(defuse_function(x))

    return jsonify(output);


def defuse_function(input):

    if int(input["n"]) <= 2:
        return 0

    n = int(input["n"])
    k = int(input["k"])
    password = input["password"]



    return input
