# divide and conquer algorithm
# it uses an auxiliary stack space


# ------- Algorithm -------
# Select a 'pivot' element - can be any element
# Place it in its correct position in the array
# Partition the array around this pivot
# Smaller elements to the left of the pivot
# Larger elements to the right of the pivot
# Repeat recursively for each subarray.

# ------- Complexity -------
# Time: O(n log n) - worst/avg/best case
# Space: O(log n) - no extra space used, but uses stack space

'''
i - from low
j - from high

let pivot = arr[low]

i             j
4 6 2 5 7 9 1 3
low           high

move i to right until arr[i] > pivot

  i           j
4 6 2 5 7 9 1 3
low           high

move j to left until arr[j] < pivot

swap arr[i] and arr[j]

  i         j
4 3 2 5 7 9 1 6
low           high

      i     j
4 3 2 5 7 9 1 6
low           high

swap arr[i] and arr[j]

        i j
4 3 2 1 7 9 5 6
low           high

when i >= j, (both cross) swap pivot and arr[j]

----- p -------
1 3 2 4 7 9 5 6
low           high

repeat the same for subarrays
- left (low to partition-1)
- right (partition + 1 to high)


'''


def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high

    while i < j:
        # find element greater than pivot and within bounds
        while arr[i] <= pivot and i <= high-1:
            i += 1
        # find element smaller than pivot and within bounds
        while arr[j] > pivot and j >= low+1:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    # place pivot in its correct position
    arr[low], arr[j] = arr[j], arr[low]

    # pivot position
    return j


def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot-1)
        quick_sort(arr, pivot+1, high)

arr = [4, 6, 2, 5, 7, 9, 1, 3]
quick_sort(arr, 0, len(arr)-1)
print(arr)