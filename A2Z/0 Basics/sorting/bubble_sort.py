# push the max to last by swapping adjacent
# gets max at end after 1 iteration

# sorting starts from right to left

# ------- Algorithm -------
# swap adjacent elements if they are in wrong order
# repeat the process for the remaining list
# each iteration pushes the maximum element to the end
# don't traverse to last element in each iteration

'''
                    i
1st iteration: 0 - n-1
2nd iteration: 0 - n-2
3rd iteration: 0 - n-3
.
.
.
n-1 iteration: 0 - 1

i begins from n-1 & goes to 1 => for i in range(n-1, 0, -1)

'''


# ------- Complexity -------
# Time: O(n^2) - worst/avg case
# Time: O(n) - best case (sorted list)
# Space: O(1) - no extra space used

# ------- Implementation -------
def bubble_sort(arr, n):
    for i in range(n-1, 0, -1):
        # don't traverse to last element
        # it will try to compare with non existing element
        for j in range(i):
            if arr[j] > arr[j + 1]:
                # swap adjacent elements
                [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]]
    return arr


print(bubble_sort([64, 25, 12, 22, 11], 5))


# optimized bubble sort - use FLAG

# if no swapping in an iteration, then list is already sorted
# break the loop in such case

def bubble_sort_optimized(arr, n):
    for i in range(n-1, 0, -1):
        flag = False
        for j in range(i):
            if arr[j] > arr[j + 1]:
                [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]]
                flag = True
        if not flag:
            break
    return arr


print(bubble_sort_optimized([1, 2, 3, 4, 5], 5))


# need to pass length, else stack will overflow
def bubble_sort_recursive(arr, n):
    if n == 1:
        return arr

    # One pass of bubble sort
    # After this pass, the largest element is moved to the end.
    for i in range(n-1):
        if arr[i] > arr[i + 1]:
            [arr[i], arr[i + 1]] = [arr[i + 1], arr[i]]

    # Largest element is fixed, recur for the remaining array
    return bubble_sort_recursive(arr, n-1)

print(bubble_sort_recursive([64, 25, 12, 22, 11], 5))
