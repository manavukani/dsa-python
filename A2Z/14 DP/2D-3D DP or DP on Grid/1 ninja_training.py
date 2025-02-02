# 3 activities, n days
# cant do same activity for 2 consecutive days
# find max merit points
# input: [[10, 40, 70], [20, 50, 80], [30, 60, 90]]
# output: 210


"""
1. express as index:
- index = day
- last = last task we did
    - 0: 0th task,
    - 1: 1th task,
    - 2: 2th last,
    - 3: NO TASK (used in TOP DOWN)
2. do stuff
- for each day, try all tasks expect last 
- for 0th day, find the max of tasks except last
3. return max value
"""


# ============== RECURRENCE ==============
def recursive(points):
    def helper(day, last):
        # for 0th day - base case
        if day == 0:
            maxi = 0
            for i in range(3):
                if i != last:
                    maxi = max(maxi, points[0][i])
            return maxi

        # for other days
        maxi = 0
        for i in range(3):
            if i != last:
                activity = points[day][i] + helper(day - 1, i)
                maxi = max(maxi, activity)
        return maxi

    n = len(points)
    return helper(n - 1, 3)  # TOP DOWN - no task done prev. for n-1 day


# ============== MEMOIZATION - TOP DOWN ==============
# TC = O(N*4*3) - N*4 states and for every state, loop iterating 3 times
# SC = O(N*4) - dp array + O(N) - recursion stack ====> O(N)
def memoization(points):
    n = len(points)
    dp = [[-1] * 4 for _ in range(n)]  # 4 choices (last), n days

    def helper(day, last):
        if dp[day][last] != -1:
            return dp[day][last]

        # base case
        if day == 0:
            maxi = 0
            for i in range(3):
                if i != last:
                    maxi = max(maxi, points[0][i])
            dp[day][last] = maxi
            return dp[day][last]

        maxi = 0
        # for all activities for current day
        for i in range(3):
            if i != last:
                activity = points[day][i] + helper(day - 1, i)
                maxi = max(maxi, activity)

        # store the maximum points
        dp[day][last] = maxi

        return dp[day][last]

    return helper(n - 1, 3)


# print(memoization([[10, 40, 70], [20, 50, 80], [30, 60, 90]]))


# ============== TABULATION - BOTTOM UP ==============
# TC = O(N*4*3) - N*4 states and for every state, loop iterating 3 times
# SC = O(N*4) - dp array  ====> O(N)
def tabulation(points):
    n = len(points)
    dp = [[-1] * 4 for _ in range(n)]

    # base case - 0th day
    # if last = 0
    dp[0][0] = max(points[0][1], points[0][2])
    # if last = 1
    dp[0][1] = max(points[0][0], points[0][2])
    # if last = 2
    dp[0][2] = max(points[0][0], points[0][1])
    # if last = 3
    dp[0][3] = max(points[0][0], max(points[0][1], points[0][2]))

    # next day onwards
    for day in range(1, n):
        for last in range(4):
            dp[day][last] = 0
            # iterate points for each day
            for task in range(3):
                if task != last:
                    activity = points[day][task] + dp[day - 1][task]
                    dp[day][last] = max(dp[day][last], activity)

    # maximum points achievable after last day with any activity
    return dp[n - 1][3]


# print(tabulation([[10, 40, 70], [20, 50, 80], [30, 60, 90]]))


# ============== SPACE OPTIMIZED ==============
"""
Looking at relation: dp[day][last] =  max(dp[day][last],points[day][task] + dp[day-1][task])
we just need previous day's data from dp
"""

# TC = O(N*4*3) - N*4 states and for every state, loop iterating 3 times ===> O(N)
# SC = O(4)
def optimal(points):
    n = len(points)
    prev = [-1] * 4

    # base case
    prev[0] = max(points[0][1], points[0][2])
    prev[1] = max(points[0][0], points[0][2])
    prev[2] = max(points[0][0], points[0][1])
    prev[3] = max(points[0][0], max(points[0][1], points[0][2]))

    for day in range(1, n):
        # store max points for each possible last activity on the current day
        temp = [0] * 4

        for last in range(4):
            temp[last] = 0
            for task in range(3):
                if task != last:
                    activity = points[day][task] + prev[task]
                    # update temp
                    temp[last] = max(temp[last], activity)

        # update 'prev' with 'temp' for next iteration.
        prev = temp

    return prev[3]
