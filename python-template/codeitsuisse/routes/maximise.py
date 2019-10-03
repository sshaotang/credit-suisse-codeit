import logging
import json

from flask import request, jsonify

from codeitsuisse import app

@app.route('/maximise_1a', methods=['POST'])
def maximise1a():
    data = request.get_json();
    return jsonify(portfolio_1a(data))

@app.route('/maximise_1b', methods=['POST'])
def maximise1b():
    data = request.get_json();
    return jsonify(portfolio_1b(data))

@app.route('/maximise_1c', methods=['POST'])
def maximise1c():
    data = request.get_json();
    return jsonify(portfolio_1c(data))


#################################################################################################


def knapSack(W , wt , val , n, name):

    # Base Case
    try:
        if n == 0 or W == 0 :
            return 0

        # If weight of the nth item is more than Knapsack of capacity
        # W, then this item cannot be included in the optimal solution
        if (wt[n-1] > W):
            return knapSack(W , wt , val , n-1, name)

        # return the maximum of two cases:
        # (1) nth item included
        # (2) not included
        else:
            return max(val[n-1] + knapSack(W-wt[n-1] , wt , val , n-1, name),
                    knapSack(W , wt , val , n-1, name))
    except:
        return val

def printknapSack(W, wt, val, n, name):
    try:
        output = []

        K = [[0 for w in range(W + 1)]
                for i in range(n + 1)]

        # Build table K[][] in bottom
        # up manner
        for i in range(n + 1):
            for w in range(W + 1):
                if i == 0 or w == 0:
                    K[i][w] = 0
                elif wt[i - 1] <= w:
                    K[i][w] = max(val[i - 1]
                    + K[i - 1][w - wt[i - 1]],
                                K[i - 1][w])
                else:
                    K[i][w] = K[i - 1][w]

        # stores the result of Knapsack
        res = K[n][W]
        w = W
        for i in range(n, 0, -1):
            if res <= 0:
                break
            # either the result comes from the
            # top (K[i-1][w]) or from (val[i-1]
            # + K[i-1] [w-wt[i-1]]) as in Knapsack
            # table. If it comes from the latter
            # one/ it means the item is included.
            if res == K[i - 1][w]:
                continue
            else:

                # This item is included.
                output.append(name[i - 1])

                # Since this weight is included
                # its value is deducted
                res = res - val[i - 1]
                w = w - wt[i - 1]
        return output
    except:
        return [name]


def portfolio_1a(input_json):
    start_capital = input_json['startingCapital']
    stocks = input_json['stocks']
    stocks_weight = [stock[2] for stock in stocks]
    stocks_value = [stock[1] for stock in stocks]
    stocks_name = [stock[0] for stock in stocks]
    profit = knapSack(start_capital, stocks_weight, stocks_value, len(stocks), stocks_name)
    portfolio = printknapSack(start_capital, stocks_weight, stocks_value, len(stocks), stocks_name)
    return {'profit': profit, 'portfolio': portfolio}

def unboundedKnapsack(W, wt, val, n):

    # dp[i] is going to store maximum
    # value with knapsack capacity i.
    try:
        dp = [0 for i in range(W + 1)]

        ans = 0

        # Fill dp[] using above recursive formula
        for i in range(W + 1):
            for j in range(n):
                if (wt[j] <= i):
                    dp[i] = max(dp[i], dp[i - wt[j]] + val[j])

        return dp[W]
    except:
        if val:
            return val[0]
        return 0

global output
output = []
def printknapSack2(W, wt, val, n, name, output):
    # dp[i] is going to store maximum
    # value with knapsack capacity i.
    try:
        dp = [0 for i in range(W + 1)]
        ans = 0
        # Fill dp[] using above recursive formula
        for i in range(W + 1):
            for j in range(n):
                if (wt[j] <= i):
                    dp[i] = max(dp[i], dp[i - wt[j]] + val[j])
        res = dp[W]
        w = W
        for i in range(n, 0, -1):
            if res <= 0:
                break
            if res == dp[i-1]:
                continue
            else:
                while wt[i-1] <= w:
                # This item is included.
                    output.append(name[i - 1])

                    # Since this weight is included
                    # its value is deducted
                    res = res - val[i - 1]
                    w = w - wt[i - 1]
        return output
    except:
        return [name]

def portfolio_1b(input_json):
    start_capital = input_json['startingCapital']
    stocks = input_json['stocks']
    stocks_weight = [stock[2] for stock in stocks]
    stocks_value = [stock[1] for stock in stocks]
    stocks_name = [stock[0] for stock in stocks]
    portfolio = []
    profit = 0
    for stock in stocks:
        start_capital -= stock[2]
        profit += stock[1]
        portfolio.append(stock[0])
    profit += unboundedKnapsack(start_capital, stocks_weight, stocks_value, len(stocks))
    portfolio += printknapSack2(start_capital, stocks_weight, stocks_value, len(stocks), stocks_name, output)
    return {'profit': profit, 'portfolio': portfolio}


def portfolio_1c(input_json):
    start_capital = input_json['startingCapital']
    stocks = input_json['stocks']
    stocks_weight = [stock[2] for stock in stocks]
    stocks_value = [stock[1] for stock in stocks]
    stocks_name = [stock[0] for stock in stocks]
    portfolio = []
    profit = 0
    profit += unboundedKnapsack(start_capital, stocks_weight, stocks_value, len(stocks))
    portfolio += printknapSack2(start_capital, stocks_weight, stocks_value, len(stocks), stocks_name, output)
    return {'profit': profit, 'portfolio': portfolio}
