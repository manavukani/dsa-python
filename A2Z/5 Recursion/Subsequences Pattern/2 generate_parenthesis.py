# TC: O(2^n) but branches does not always split into 2, so it's less than 2^n
# SC: O(2*n) = O(n)

"""
Generate each combination by either adding an opening ( or a closing ) parenthesis with constraints:

- NEVER add more than n opening or n closing
- Number of closing NEVER EXCEEDS number of opening

"""


# recursive solution
def generateParenthesis(n):
    result = []

    def backtrack(current, open_count, close_count):
        # BASE CASE - when both open and close == n
        if open_count == n and close_count == n:
            result.append(current)
            return

        # only add if open < n
        if open_count < n:
            backtrack(current + "(", open_count + 1, close_count)
        # only close if close < open
        if close_count < open_count:
            backtrack(current + ")", open_count, close_count + 1)

    backtrack("", 0, 0)
    return result


# pick, not pick recusrive backtrack solution
def generateParenthesis(n):
    stack = []
    res = []

    def backtrack(opened, closed):
        # BASE CASE - when both open and close == n
        if opened == closed == n:
            res.append("".join(stack))
            return
        # only add if open < n
        if opened < n:
            stack.append("(")
            backtrack(opened + 1, closed)
            stack.pop()
        # only close if close < open
        if closed < opened:
            stack.append(")")
            backtrack(opened, closed + 1)
            stack.pop()

    backtrack(0, 0)
    return res


print(generateParenthesis(3))
