def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1

    # storing elements in the temporary array in a sorted manner
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    # if elements on the left half are still left
    while left <= mid:
        temp.append(arr[left])
        left += 1

    # if elements on the right half are still left
    while right <= high:
        temp.append(arr[right])
        right += 1

    # transferring all elements from temporary to arr
    for i in range(low, high + 1):
        arr[i] = temp[i - low]


def merge_sort(arr, low, high):
    if low >= high:
        return
    mid = (low + high) // 2
    merge_sort(arr, low, mid)  # left half
    merge_sort(arr, mid + 1, high)  # right half
    merge(arr, low, mid, high)  # merging sorted halves

arr = [9, 4, 7, 6, 3, 1, 5]
n = len(arr)
merge_sort(arr, 0, n - 1)
print(arr)
