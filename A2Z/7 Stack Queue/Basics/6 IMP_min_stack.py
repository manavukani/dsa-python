"""
Requirement: push, pop, top, getMin --> O(1)

NEETCODE APPROACH:

- PUSH:
    - empty stack: push 0 and set min to x
    - non-empty stack: push x - min and update min if x < min

- WHY PUSH x - min?
    - if x is less than min
        - we need to update min,
        - cause diff will be -ve
    - if x is greater than min
        - we don't need to update min,
        - cause diff will be +ve

- POP:
    - pop from stack
    - if pop is -ve (it was current min, when pushed)
        - update min, retrieve old min (previous_min = self.min - pop)

- WHY THIS WORKS?
    - Since `pop = x - previous_min`
    - and `x < previous_min`
    - rearranging gives `previous_min = x - pop`
    - `self.min` is currently `x`
    - so, `previous_min = self.min - pop`.

- TOP:
    - if top is +ve, return top + min
    - if top is -ve, return min

- GETMIN:
    - return min
"""

# 1. brute force
# push, pop, top --> O(1)
# getMin() --> O(n)


# 2. two stacks
# all ops --> TC: O(1)
# SC: O(2n)
class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # if stack is empty, val is the min
        # if not, take min
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# 3. one stack --------------- IMP
# all ops --> TC: O(1)
# SC: O(n)
class MinStack:
    def __init__(self):
        self.min = float("inf")
        self.stack = []

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = x
        else:
            self.stack.append(x - self.min)
            if x < self.min:
                self.min = x

    def pop(self) -> None:
        if not self.stack:
            return

        pop = self.stack.pop()

        if pop < 0:
            self.min = self.min - pop

    def top(self) -> int:
        top = self.stack[-1]
        if top > 0:
            return top + self.min
        else:
            return self.min

    def getMin(self) -> int:
        return self.min
