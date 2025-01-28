class Solution:
    def dailyTemperatures(self, temperatures):
        res = [0] * len(temperatures)
        stack = []  # temperature, index

        for index, value in enumerate(temperatures):
            # pop until new > top
            # updated result value for that temperature
            while stack and value > stack[-1][0]:
                stackVal, stackInd = stack.pop()
                res[stackInd] = index - stackInd

            # add new temperature to stack
            stack.append((value, index))

        return res
