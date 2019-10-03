import logging
import json
import random

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

# 25,75,25,75,25,75,25,75,25,75
@app.route('/lottery', methods=['GET'])
def lottery():
    du_shen_lai_liao = []
    for i in range(10):
        du_shen_lai_liao.append(random.randrange(0,100))
    return jsonify([30,70,40,10,90,30,20,80,60,40]);
