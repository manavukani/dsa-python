from typing import List

# swap each non-zero element with the element at last_non_zero_index,
# which tracks the position of the last non-zero element.

# better - single pass => fast


def solve(n: int, nums: List[int]) -> List[int]:
    last_non_zero_index = 0
    for i in range(n):
        if nums[i] != 0:
            nums[last_non_zero_index], nums[i] = nums[i], nums[last_non_zero_index]
            last_non_zero_index += 1
    return nums

print(solve(8, [0, 0, 1, 2, 0, 4, 0, 1]))


# striver approach
'''
The first loop finds the first zero in the array and sets j to its index.
If no zero is found, it returns the array as is.
The second loop swaps each non-zero element found after the first zero with the element at index j, 
then increments j.
'''
def move_zeros(n: int, a: List[int]) -> List[int]:
    j = -1
    # Place the pointer j
    for i in range(n):
        if a[i] == 0:
            j = i
            break

    # No non-zero elements
    if j == -1:
        return a

    # Move the pointers i and j and swap accordingly
    for i in range(j + 1, n):
        if a[i] != 0:
            a[i], a[j] = a[j], a[i]
            j += 1

    return a


arr = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
n = 10
ans = move_zeros(n, arr)
for it in ans:
    print(it, end=' ')
print()
