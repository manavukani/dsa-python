def solve(candies, extraCandies):
    highestCount = max(candies)
    res = [False]*len(candies)
    for i in range(len(candies)):
        if candies[i] + extraCandies >= highestCount:
            res[i] = True
    return res