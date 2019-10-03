import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/bankbranch', methods=['POST'])
def bankbranch():
    data = request.get_json()
    print(data)
    return jsonify(bank(data));


def bank(input_json):
    officers_time = input_json["branch_officers_timings"]
    n = input_json["N"]
    officerMap = {}
    serving = {}
    for i in range(len(officers_time)):
        officerMap[i+1] = officers_time[i]
        serving[i+1] = 0
    maxTime = n*max(officers_time)
    officer_available = [i+1 for i in range(len(officers_time))]
    # officer_justreturned = [False for i in range(len(officers_time))]
    time = 0
    customer = 0
    while time < maxTime:
        for j in range(len(officers_time)):
            if (j+1) not in officer_available:
                if serving[j+1] == officerMap[j+1]:
                    serving[j+1] = 0
                    officer_available.append(j+1)
                    # officer_justreturned[j] = True
                    officer_available = sorted(officer_available)
                else:
                    serving[j+1] += 1
            # else:
            #     officer_justreturned[j] = False
        if customer < n:
            customer += 1
            k = 0
            while officer_available and (n-customer) > 0:
                # try:
                #     if not officer_justreturned[officer_available[k]-1]:
                #         officer_available.pop(k)
                #     else:
                #         k += 1
                # except IndexError:
                #     break
                try:
                    officer_available.pop(k)
                except:
                    break
                k += 1

        else:
            return {'answer':officer_available[0]}
        # print(officer_available)
        # print(serving)
        time += 1
