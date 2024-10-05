# ---------M1---------
# Time = O(n), Space = O(n)
def brute_force(nums, k):
    length = len(nums)
    
    if length == 0:
        return nums

    k = k % length

    while k > 0:
        pick = nums[-1]  # last element
        # Shift all to right
        for i in range(length - 1, 0, -1):
            nums[i] = nums[i - 1]
        nums[0] = pick  # Place last element at start
        k -= 1

    return nums

# ---------M2---------
# Time = O(n), Space = O(k)
def optimize_brute(nums, k):
    n = len(nums)

    if n == 0:
        return

    k = k % n

    if k == 0:
        return

    # store the last k elements
    temp = nums[-k:]

    # shift the remaining elements to the right by k
    for i in range(n - k - 1, -1, -1):
        nums[i + k] = nums[i]

    # copy from temp to start of the original numsay
    for i in range(k):
        nums[i] = temp[i]

    print(nums)

# ---------M3---------
# Time = O(n), Space = O(1)
def rotate_optimal(nums, k) -> None:
    k %= len(nums)
    def reverse(left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
            
    # right shift
    reverse(0, len(nums) - 1)   # entire
    reverse(0, k - 1)           # first
    reverse(k, len(nums) - 1)   # second
    
    # for left shift - first, second, entire
    

nums = [1, 2, 3, 4, 5, 6, 7]
rotate_optimal(nums,3)
print(nums)


# Using reversed()
def using_python_functions (nums, k) -> None:
    n = len(nums)
    k = k % n
    # nums.reverse()
    nums[:] = list(reversed(nums))
    nums[:k] = list(reversed(nums[:k]))
    nums[k:] = list(reversed(nums[k:]))

nums = [1, 2, 3, 4, 5, 6, 7]
using_python_functions(nums,3)
print(nums)

'''
reverse():
This method reverses the list in place, meaning it modifies the original list directly and returns None.

reversed():
This function returns an iterator that accesses the list elements in reverse order without modifying the original list.
You need to convert it to a list (or another collection) if you want to see the reversed sequence.

'''