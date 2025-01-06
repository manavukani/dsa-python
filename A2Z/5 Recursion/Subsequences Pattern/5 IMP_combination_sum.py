# subsequence sub = target
# TWIST: can use the same element multiple times

# TC: Exponential
# Approx: O(2^t * k) where t is the target and k is avg length of the subsequence
# WHY: 2^t for each element we have 2 choices: include or exclude.
# If element is 1, tarfet is 10, we can have 10 pick/not pick at max.
# SC: cannot say for sure, depends on case to case


def solve(arr, target):

    ans = []
    ds = []

    def combination_sum(target, idx):
        if idx == len(arr):
            if target == 0:
                """IMP: copy coz using same ds for all the recursive calls"""
                ans.append(ds.copy())
            return

        # pick
        if arr[idx] <= target:
            ds.append(arr[idx])
            """IMP: no increment in idx bcoz can pick same multiple times"""
            combination_sum(target - arr[idx], idx)
            ds.pop()

        # not pick
        combination_sum(target, idx + 1)

        return ans

    combination_sum(target, 0)

    return ans


print(solve([2, 3, 6, 7], 7))  # [[2, 2, 3], [7]]
