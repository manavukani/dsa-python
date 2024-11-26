def generateParenthesis(n):
    stack = []
    res = []

    def backtrack(opened, closed):
        # only add if open < n
        # only close if close < open
        # valid IFF open = close = n ====> base case
        if opened == closed == n:
            res.append("".join(stack))
            return
        if opened < n:
            stack.append('(')
            backtrack(opened + 1, closed)
            stack.pop()
        if closed < opened:
            stack.append(")")
            backtrack(opened, closed + 1)
            stack.pop()
    backtrack(0, 0)
    return res


print(generateParenthesis(3))
# ["((()))","(()())","(())()","()(())","()()()"]


# def dynamic_prog(self, n):
#     res = [[] for _ in range(n+1)]
#     res[0] = [""]

#     for k in range(n + 1):
#         for i in range(k):
#             for left in res[i]:
#                 for right in res[k-i-1]:
#                     res[k].append("(" + left + ")" + right)

#     return res[-1]
