import logging
import json

from flask import request, jsonify

from codeitsuisse import app

@app.route('/encryption', methods=['POST'])
def encryption():
    data = request.get_json();
    print(data)
    return jsonify(sian(data));



def sian(input):

    output = []
    for blk in input:

        checker = 0
        nblk = ""
        for el in blk["text"]:
            if el != " " and el.isalpha():
                nblk += el.upper()

#        print(nblk)


        if len(nblk) == 0:
            print("hop!")
            checker = 1

        x = ""

        origin = 0
        n = blk["n"]

        if (n > len(nblk)):
#            print(nblk)
            output.append(nblk)
            checker = 1

        if checker == 0:
            segments = []
    #        print(len(nblk))
            if len(nblk) % n != 0:
                segcnt = len(nblk) // n + 1
            else:
                segcnt = (len(nblk) // n)

    #        print(segcnt)

            for s in range(segcnt):
                segments.append([])

    #        print(segments)

            r = 0
            for el in nblk:
                segments[r].append(el)
                if r == segcnt-1:
                    r = 0
                else:
                    r += 1

    #        print(segments)
            e = ""
            for a in segments:
                e += ''.join(a)
            output.append(e)

    print(len(output))
    return output
