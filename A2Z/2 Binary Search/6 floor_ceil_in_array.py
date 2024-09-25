# floor = largest number <= x
# ceil = smallest number >= x ---------> LOWER BOUND
# not found return -1

arr = [10, 20, 30, 40, 50]
x = 25
# floor = 20, ceil = 30


def findFloor(arr, x):
    low = 0
    high = len(arr) - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2
        # maybe an answer
        if arr[mid] <= x:
            ans = arr[mid]
            # look for larger index on the right
            low = mid + 1
        else:
            high = mid - 1  # look on the right

    return ans


def findCeil(arr, x):
    low = 0
    high = len(arr) - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2
        # maybe an answer
        if arr[mid] >= x:
            ans = arr[mid]
            # look for smaller index on the left
            high = mid - 1
        else:
            low = mid + 1  # look on the right

    return ans


def getFloorAndCeil(arr, x):
    f = findFloor(arr, x)
    c = findCeil(arr, x)
    return (f, c)


ans = getFloorAndCeil(arr, x)
print("The floor and ceil are:", ans[0], ans[1])

# eventually you will understand we dont need "ans",
# either "low" or "high" will be the answer
