# Given an integer array arr of size N, sorted in ascending order (with distinct values)
# Target = k. Now the array is rotated at some pivot point unknown to you.
# Find the index at which k is present and if k is not present return -1.

# IMP - The array has distinct values.

def brute_force(arr, target):
    '''
    The brute force approach is to iterate through the array and find the target.
    '''
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# O(logN) time | O(1) space
def binary_search(arr, target):
    '''
    Since it is not known where the array is rotated, we need to check at each step
    if the target is in the array is left or right sorted.
    '''
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        # case 1 - low half is sorted
        # left side element should be less than right side element
        if arr[low] <= arr[mid]:
            # check if target is within the range of low and mid
            if arr[low] <= target and target <= arr[mid]:
                high = mid - 1
            else:
                low = mid + 1

        # case 2 - high half is sorted
        else:
            # check if target is within the range of mid and high
            if arr[mid] <= target and target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    # not found
    return -1


arr = [4, 5, 6, 7, 0, 1, 2]
target = 5
print(binary_search(arr, target))  # 4
