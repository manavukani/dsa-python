# ip - rating values of n children standing in a line

"""
TODO:
   1. Each child must have at least one candy.
   2. Children with a higher rating get more candies than their neighbors.
"""
# op - minimum candies to satisfy both conditions


# brute force
"""
1. First iteration - going forward
    Check if current is bigger than previous
    if so, give 1 more candy than previous
2. Second iteration - going backwards
    Check if current is bigger than next one (technically previous in reverse dir)
    if so, give 1 more candy than next one (technically previous in reverse dir)
3. Take maximum for each index

Eg:

ratings =  1  3  2  1
1st itr:   1  2  1  1  (left to right)
2nd itr:   1  3  2  1  (right to left)


"""


# TC = O(3N), SC = O(2N)
def brute(ratings):
    # initiate array for both iterations
    candies_left = [0] * len(ratings)
    candies_right = [0] * len(ratings)

    # check left neighbors
    for i in range(len(ratings)):
        if i == 0:
            candies_left[i] = 1  # no left neighbor
        elif ratings[i - 1] < ratings[i]:
            candies_left[i] = candies_left[i - 1] + 1
        else:
            candies_left[i] = 1

    # check right neighbors
    for i in range(len(ratings) - 1, -1, -1):
        if i == len(ratings) - 1:
            candies_right[i] = 1  # no right neighbor
        elif ratings[i] > ratings[i + 1]:
            candies_right[i] = candies_right[i + 1] + 1
        else:
            candies_right[i] = 1

    # take max of both
    final = list(zip(candies_left, candies_right))
    return sum([max(l, r) for l, r in final])


print(brute([1, 3, 2, 1]))


# optimized brute -----> TC = O(2N), SC = O(N)
"""
eliminate need of right and separately summation
calculate left then find max of left and right for each index and do rolling sum
"""


def optimized_brute(ratings):
    n = len(ratings)
    candies_left = [0] * n
    candies_left[0] = 1

    # 1st iteration
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies_left[i] = candies_left[i - 1] + 1
        else:
            candies_left[i] = 1

    # 2nd iteration and total candies count (max)
    total = max(1, candies_left[-1])  # add the last element
    right = 1  # candy = 1 for the last child
    # for the rest of 'em
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            right += 1
        else:
            right = 1

        # rolling sum
        total += max(candies_left[i], right)

    return total


print(optimized_brute([1, 3, 2, 1]))


# --------------- OPTIMAL ------------- SLOPE APPROACH
"""
we just care about the total candies, keep rooling sum
- increasing slope - we assign 1 2 3 4 ... (store PEAK when slope stops)
- decreasing slope - we AGAIN assign 1 2 3 4...  (store DOWN when slope stops) and check max for peak and down
    - since we already have added PEAK to sum, add the difference if DOWN > PEAK
- plateau - just give 1 each
"""


# TC = O(N), SC = O(1)
def optimal(ratings):
    total = 1  # already added 1st ele
    i = 1  # start from 2nd ele
    n = len(ratings)
    # for rest
    while i < n:
        # NO SLOP - give 1 candy  to all
        if ratings[i] == ratings[i - 1]:
            total += 1
            i += 1
            continue
        
        # HAVE SLOPE
        peak = 1
        # if ratings are increasing add prev candies +1 to sum
        while i < n and ratings[i] > ratings[i - 1]:
            peak += 1
            total += peak
            i += 1
        down = 1
        # if rating are decreasing add 1,2,3 etc to sum 
        while i < n and ratings[i] < ratings[i - 1]:
            total += down
            down += 1
            i += 1

        if down > peak:
            total += down - peak  # difference

    return total


print(optimal([1, 3, 2, 1]))
