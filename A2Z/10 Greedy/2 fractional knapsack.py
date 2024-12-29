# weight, value, capacity
# find the maximum value we can fill of the knapsack (can take fraction of the item)

def fractional_knapsack(weight, value, capacity):
    ratio = [v/w for v, w in zip(value, weight)]
    arr = sorted(zip(ratio, weight, value), reverse=True)
    max_value = 0
    
    for r, w, v in arr:
        if w <= capacity:
            max_value += v
            capacity -= w
        else:
            max_value += v * capacity / w
            break
    return max_value

# Test
weight = [10, 20, 30]
value = [60, 100, 120]
capacity = 50

print(fractional_knapsack(weight, value, capacity)) # 240.0


# 0/1 knapsack fails with greedy approach, we need to use dynamic programming