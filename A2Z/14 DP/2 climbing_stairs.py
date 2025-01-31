class RecursiveSolution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 1

        # left and right sub tree for recursion
        left = self.climbStairs(n - 1)
        right = self.climbStairs(n - 2)

        return left + right


# Notice - It's similar to Fibonnaci recursion


class SpaceOptimizedSolution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 1

        for i in range(n - 1):
            tmp = one
            one = one + two
            two = tmp

        return one
