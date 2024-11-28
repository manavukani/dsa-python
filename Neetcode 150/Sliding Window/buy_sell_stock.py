def maxProfit(prices):
    maxPro = 0
    minEle = prices[0]
    for p in prices:
        minEle = min(minEle, p)
        maxPro = max(maxPro, p - minEle)
    return maxPro