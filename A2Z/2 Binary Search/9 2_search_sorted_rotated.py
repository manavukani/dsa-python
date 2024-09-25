# Given an integer array arr of size N, sorted in ascending order (with distinct values) and
# a target value k. Now the array is rotated at some pivot point unknown to you.

# TODO: RETURN => TRUE if k is present in the array, else FALSE.
# NOTE: JUST ONE CHANGE => IT MAY HAVE DUPLICATES

def brute_force(arr, target):
    '''
    The brute force approach is to iterate through the array and find the target.
    '''
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


'''
old solution would work for some cases but not all
WORKS: [4,5,1,2,3,3,4,4] and target = 4, left is not sorted => 4 is in left


FAILING CASE: [3,1,2,3,3,3,3] and target = 2

low = 3
high = 3
mid = 3

APPROACH:
1. Find the mid element
2. Check if the mid == target
    3. If yes, return mid  
4. If not, check if the left = right = mid
    5. If yes, then shrink search space by excluding left and right (coz mid != target, so left and right are not target)
6. Check if left or right is sorted
'''


# O(log N) for most
# O(N/2) for worst case when almost all elements are same
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return True

        if arr[mid] == arr[low] == arr[high]:
            low += 1
            high -= 1
            continue  # skip the rest of the loop and start from the beginning

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
    return False


arr = [3,1,2,3,3,3,3]
target = 2
print(binary_search(arr, target))  # True
