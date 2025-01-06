# BRUTE: pick/not-pick for all subset, use a set to store unique


# BETTER: when we not pick, skip over duplicate elements (for this sort array in beginning)
# TC: O(N * 2^N)

def unique_subsets(nums):
    nums.sort()
    ans = []

    def backtrack(i, ds):
        if i == len(nums):
            ans.append(ds[::]) # same as deep copy
            return

        # pick
        ds.append(nums[i])
        backtrack(i + 1, ds)
        ds.pop()

        # skip over duplicate elements - similar to combination sum 2
        while i + 1 < len(nums) and nums[i + 1] == nums[i]:
            i += 1

        # not pick
        backtrack(i + 1, ds)

    backtrack(0, [])
    return ans


arr = [1, 2, 2]
print(unique_subsets(arr))
