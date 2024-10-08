# 2 3 -2 4
# ans = 6

# brute
# n^3
def brute(arr):
    n = len(arr)
    maxi = 1
    for i in range(n):
        for j in range(i, n):
            prod = 1
            for k in range(i, j):
                prod = prod * arr[k]
            maxi = max(prod, maxi)
    return maxi


# n^2
def better(arr):
    n = len(arr)
    maxi = 1
    for i in range(n):
        prod = 1
        for j in range(i, n):
            prod = prod * arr[j]
            maxi = max(prod, maxi)
    return maxi



# FAILS FOR 0
def can_do(arr):
    maxi = float('-inf')
    prefix, suffix = 1, 1
    for i in range(len(arr)):
        prefix *= arr[i]
        maxi = max(prefix, maxi)
    for j in range(len(arr)-1, -1, -1):
        suffix *= arr[j]
        maxi = max(suffix, maxi)
    return maxi

test = [-3,0,1,-2]
print(can_do(test)) # gives 0 but expected 1


# kadane is not intutive in this
# we use OBSERVATION BASED:
'''

1) ALL POSITIVE: product of all [2,3,5,4,6]

2) EVEN # OF -VE: product of all [2,4,-2,3,-6]

3) ODD # OF -VE: 

if 3 -ve => remove one -ve

[3  2  -1  4  -6  3  -2  6]
_____      ________________
prefix  x           suffix  => remove -1


4) HAS ZEROES

[-2 3 1 0 -2 3 4 0 1 4 0 4 6 -1]
_______   ______   _____________

Doesn't make sense to include 0

Divide into sub-parts and consider as separate array => find max(3 parts)

Whenever we encouter => carry it into 1 for fresh start for next part

'''

def optimal(arr):
    maxi = float('-inf')
    prefix, suffix = 1, 1
    for i in range(len(arr)):
        # handling cases with zero
        if prefix == 0:
            prefix = 1
        if suffix == 0:
            suffix = 0
        # simultaenously calculate prefix and suffix
        prefix *= arr[i]
        suffix *= arr[len(arr) - 1 - i]
        maxi = max(maxi, max(prefix, suffix))
    return maxi