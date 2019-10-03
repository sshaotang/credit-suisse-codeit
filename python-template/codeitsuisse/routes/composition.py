import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;


@app.route('/composition', methods=['POST'])
def composition():
    data = request.get_json();
    return json.dumps(comp(data));


def comp(input_json):
    output = []
    for item in input_json:
        testId = item['setId']
        compo = item['composition']
        patterns = item['patterns']
        result = 0
        for pattern in patterns:
            result += compo.count(pattern) - 1
            result += compo.count(pattern[::-1]) -1
            compo = compo.strip(pattern[0])
        output.append({"testId":testId,"result":result})
    return output
