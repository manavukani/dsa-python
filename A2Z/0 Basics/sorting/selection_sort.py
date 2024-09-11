# just as name suggests - select minimum
# gets min at start after 1 iteration

# sorting starts from left to right

# ------- Algorithm -------
# traverse through the list
# find the minimum element
# swap it with the first element
# repeat the process for the remaining list

# ------- Complexity -------
# Time: O(n^2) - for all cases
# Space: O(1) - no extra space used

# ------- Implementation -------
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
            # Swap new minimum element, if index are different
        if min_index != i:
            [arr[i], arr[min_index]] = [arr[min_index], arr[i]]
    return arr

print(selection_sort([64, 25, 12, 22, 11]))
