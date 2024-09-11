# divide & merge

# ------- Algorithm -------
# divides the given array into equal parts
# merges the 2 sorted parts
# repeat the process for the remaining parts

# ------- Complexity -------
# Time: O(n log(n)) - worst/avg/best case
# Space: O(n) - no extra space used

# ------- Implementation -------

def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2  # floor

    # divide
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # conquer
    return merge(left, right)


def merge(left, right):
    arr = [0] * (len(left) + len(right))
    i = j = k = 0

    # i = left
    # i = right
    # k = arr

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    # add remaining elements
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return arr

arr = [64, 25, 12, 22, 11]
print(merge_sort(arr))
