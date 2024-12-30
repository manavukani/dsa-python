# Three char - ( ) *
# * can be used as "(" or ")" or ""

"""
for normal parenthesis string, we can use counter to check if it is valid or not
increment counter for "(" and decrement for ")"
if counter is negative at any point, return False --- invalid eg: "())("
if counter is 0 at the end, return True --- valid eg: "(()())"
"""


# BRUTE FORCE ---- TC = O(3^n), SC = O(N)
# for * , we can check for all 3 possibilities, return True if any of them is True
def checkValidString(s):
    def helper(s, idx, count):
        if count < 0:
            return False
        if idx == len(s):
            return count == 0
        if s[idx] == "(":
            return helper(s, idx + 1, count + 1)
        if s[idx] == ")":
            return helper(s, idx + 1, count - 1)
        if s[idx] == "*":
            return (
                helper(s, idx + 1, count + 1)
                or helper(s, idx + 1, count - 1)
                or helper(s, idx + 1, count)
            )

    count = 0
    return helper(s, 0, count)


"""
MODIFIED BRUTE --- IMP to discuss brute first in interview

-   Maintain the range in form of min and max -- all possible outcomes
-   When * comes, +1 the max, -1 the min (don't go negative - as its not valid)

========== TC = O(N), SC = O(1) ==========
"""


def solve(s):
    mini, maxi = 0, 0
    for char in s:
        if char == "(":
            mini += 1
            maxi += 1
        if char == ")":
            mini -= 1
            maxi -= 1
        if char == "*":
            mini -= 1
            maxi += 1

        # keep mini above 0 (we dont care for -ve ones as they are NP)
        mini = max(0, mini)

        # no valid cases possible
        # eg: ")" min = -1, max = -1, cannot compare
        if maxi < 0:
            return False

    # something positive is possible
    return mini == 0


# Dynamic Prog  ----> DP[n][n] --> TC = O(n^2), SC = O(N^2) {can be reduced to linear space}
