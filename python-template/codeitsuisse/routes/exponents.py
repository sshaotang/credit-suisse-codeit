import logging
import json

from flask import request, jsonify

from codeitsuisse import app

import math

def last_digit(number, power):
    return pow(number,power,10)

def first_digit(number,power):
    log = power*(math.log(number,10))
    fractional = log - int(log)
    temp = 10**fractional
    return str(temp)[0]


def exponents(input_json):
    # for item in input_json:
    # number = item['n']
    # power = item['p']
    number = input_json['n']
    power = input_json['p']
    if number % 10 == 0:
        return {'result': [1,power+1,0]}
    elif number != 0 and number < (10**9):
        first = first_digit(number,power)
        last = last_digit(number,power)
        length = math.ceil(power*(math.log(number, 10)))
        return {'result':[int(first),length,int(last)]}
    else:
        return {'result': [0,1,0]}

@app.route('/exponent', methods=['POST'])
def expo():
    data = request.get_json();
    print(data)
    return jsonify(exponents(data));
