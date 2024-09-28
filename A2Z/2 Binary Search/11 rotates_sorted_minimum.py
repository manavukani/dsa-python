# Rotated sorted array minimum [unique elements]

# NAIVE APPROACH: O(N) - iterate through the array and find the minimum element

# OPTIMAL APPROACH: O(log N) - binary search

'''
1. Find which half is sorted
2. Unsorted half may have the minimum element

4 5 6 7 0 1 2
l     m     h
WORKS - left is sorted => right has the minimum element

7 8 1 2 3 4 5 6
l     m       h
WORKS - right is sorted => left has the minimum element

4 5 1 2 3
l   m   h
FAILS - right is sorted => but has the minimum element

1 2
l h
m
FAILS - left is sorted => but has the minimum element

3. pick minimum and eliminate

'''


def binary_search(arr):
    low = 0
    high = len(arr) - 1
    ans = float('inf')
    while low <= high:
        mid = low + (high - low) // 2
        
        # optimization - if the array is already sorted
        if arr[low] <= arr[high]:
            return min(arr[low], ans)
        
        # case 1 - low half is sorted
        if arr[low] <= arr[mid]:
            ans = min(arr[low], ans)
            low = mid + 1
        # case 2 - high half is sorted
        else:
            ans = min(arr[mid], ans)
            high = mid - 1

    return ans


arr = [4, 5, 6, 0, 1, 2]
print(binary_search(arr))  # 0
