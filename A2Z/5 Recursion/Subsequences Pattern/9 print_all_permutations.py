# ip - [1,2,3]
# op = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]] = 3! = 6


def permute(nums):
    """
    APPROACH 1: BACKTRACKING

    - backtracking approach to build permutations
    - maintain temporary list and visited array
    - Each complete permutation is appended to ans, when length all elements are visited (len(ds) == len(nums))
    """

    ans = []
    visited = [False] * len(nums)
    ds = []

    def recurse(ds):
        if len(ds) == len(nums):
            ans.append(ds[::])
            return

        # for each element, if not visited --> generate all permutations with it as starting element
        for i in range(len(nums)):
            if not visited[i]:
                visited[i] = True
                ds.append(nums[i])
                recurse(ds)  # recurse
                ds.pop()
                visited[i] = False

        return ans

    return recurse(ds)


arr = [1, 2, 3]
print(permute(arr))


"""
APPROACH 2: SWAPPING

- swap each element with every other element including / after it
- backtrack
- swap back to original position
- TC: O(n! * n)
- SC: O(n)

https://youtu.be/f2ic2Rsc9pU
"""


def swapping(nums):

    ans = []

    def recurse(idx):
        if idx >= len(nums):
            ans.append(nums[::])
            return

        for i in range(idx, len(nums)):
            nums[i], nums[idx] = nums[idx], nums[i]  # swap
            recurse(idx + 1)  # recurse
            nums[i], nums[idx] = nums[idx], nums[i]  # swap back

        return ans

    return recurse(0)


arr = [1, 2, 3]
print(swapping(arr))
