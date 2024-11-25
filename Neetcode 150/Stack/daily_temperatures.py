# days on right with higher temperature

# INPUT = [73, 74, 75, 71, 69, 72, 76, 73]
# OUTPUT = [1, 1, 4, 2, 1, 1, 0, 0]

# TC = O(n^2)
def brute_force(temperatures):
    n = len(temperatures)
    result = [0] * n
    for i in range(n):
        # check for each element on right
        for j in range(i+1, n):
            if temperatures[j] > temperatures[i]:
                result[i] = j - i
                break
    return result

# using stack, TC = O(n)
# push till we find greater element, pop till smaller

def dailyTemperatures(temperatures):
    res = [0] * len(temperatures) # default 0 so no need to update if no greater element
    stack = []  # pair: [temp, index]
    for idx, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            stackT, stackInd = stack.pop()
            res[stackInd] = idx - stackInd
        stack.append((t, idx))
    return res
