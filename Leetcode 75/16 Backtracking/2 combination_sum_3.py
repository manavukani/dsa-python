class Solution:
    def combinationSum3(self, k, n):
        ans = []

        # explore every combination of 1..9
        def backtrack(start, target, ds):
            if len(ds) == k:
                if target == 0:
                    ans.append(ds[:])
                return

            for i in range(start, 10):
                if i > target:  # stop early, out of bounds
                    break
                ds.append(i)
                backtrack(i + 1, target - i, ds)
                ds.pop()

        backtrack(1, n, [])
        return ans
