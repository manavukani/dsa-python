# Given an array consisting of only 0s, 1s, and 2s. Write a program
# to in-place sort the array without using inbuilt sort functions.
# ( Expected: Single pass-O(N) and constant space)

# brute force approach => sorting => O(nlogn)
def brute(arr):
    arr.sort()
    return arr

# better approach => counting => O(2n)
# for loop -> count 0, 1, 2
# 1 for loop for each -> append 0, 1, 2
def better(arr):
    cnt_0, cnt_1, cnt_2 = 0, 0, 0
    for i in arr:
        if i == 0:
            cnt_0 += 1
        elif i == 1:
            cnt_1 += 1
        else:
            cnt_2 += 1
    for i in range(cnt_0):
        arr[i] = 0
    for i in range(cnt_0, cnt_0+cnt_1):
        arr[i] = 1
    for i in range(cnt_0+cnt_1, cnt_0+cnt_1+cnt_2):
        arr[i] = 2
    return arr

# optimal approach => 3 pointers
# Dutch National Flag Algorithm

# 0 -> low -1 = 0
# low -> mid -1 = 1
# mid -> high -1 = 2

def optimal(arr):
    l, m = 0, 0
    h = len(arr) - 1
    while m <= h:
        if arr[m] == 0:
            arr[l], arr[m] = arr[m], arr[l]
            l += 1
            m += 1
        elif arr[m] == 1:
            m += 1
        else:
            arr[m], arr[h] = arr[h], arr[m]
            h -= 1
    return arr

n = 6
arr = [0, 2, 1, 2, 0, 1]
optimal(arr)
print("After sorting:")
for num in arr:
    print(num, end=" ")
print()