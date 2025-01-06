# combinations of 'k' numbers that sum up to 'n' with conditions:
# - Only numbers 1 through 9 are used.
# - Each number is used at most once.
# Return a list of all possible valid combinations. The list must not contain duplicates, any order.


'''
APPROACH: BACKTRACKING

- Start from a given number (1 through 9).
- Loop through possible choices and pick each number once.
- Use appending and popping for backtracking.
- Stop early if the current number exceeds the target.
'''

# Time Complexity: O(9^k)
# Space Complexity: O(k)
def combination_sum_3(k: int, n: int):
    ans = []

    # explore every combination of 1..9 exactly k items, summing to n
    def backtrack(start, target, ds):
        if len(ds) == k:
            if target == 0:
                ans.append(ds[:])
            return

        for i in range(start, 10):
            if i > target:
                break
            ds.append(i)
            backtrack(i + 1, target - i, ds)
            ds.pop()

    backtrack(1, n, [])
    return ans


print(combination_sum_3(9, 45))
