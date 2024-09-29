# array of prices where prices[i] is the price of a given stock on an ith day.
# maximize profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit. If you cannot achieve any profit, return 0.

# [7,1,5,3,6,4] => 5
# [7,6,4,3,1] => 0

def brute(arr):
    maxPro = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] > arr[i]:
                maxPro = max(arr[j] - arr[i], maxPro)
    return maxPro


# for max profit we need to check difference of each element with minimum element
def optimal(arr):
    minEle = arr[0]
    maxPro = 0
    for price in arr:
        minEle = min(minEle, price)
        maxPro = max(maxPro, price - minEle)
    return maxPro


print(optimal([7, 1, 5, 3, 6, 4]))
print(optimal([7, 6, 4, 3, 1]))
