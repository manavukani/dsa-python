# Time = O(n), Space = O(n)
def brute_force(arr, k):
    length = len(arr)
    
    if length == 0:
        return arr

    k = k % length

    while k > 0:
        pick = arr[-1]  # last element
        # Shift all to right
        for i in range(length - 1, 0, -1):
            arr[i] = arr[i - 1]
        arr[0] = pick  # Place last element at start
        k -= 1

    return arr

# Time = O(n), Space = O(k)
def optimize_brute(arr, k):
    n = len(arr)

    if n == 0:
        return

    k = k % n

    if k == 0:
        return

    # store the last k elements
    temp = arr[-k:]

    # shift the remaining elements to the right by k
    for i in range(n - k - 1, -1, -1):
        arr[i + k] = arr[i]

    # copy from temp to start of the original array
    for i in range(k):
        arr[i] = temp[i]

    print(arr)

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
    

arr = [1, 2, 3, 4, 5, 6, 7]
rotate_optimal(arr,3)
print(arr)
