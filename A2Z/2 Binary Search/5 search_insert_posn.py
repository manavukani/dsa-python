# for sorted array [1,2,4,6,7], find a position to insert x

# same as LOWER BOUND

def insert_loc(arr, x):
    low = 0
    high = len(arr) - 1
    ans = len(arr)

    while low <= high:
        mid = (low+high)//2

        if arr[mid] >= x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans


arr = [1, 2, 4, 6, 7]
x = 2
print("Index to insert", x, ":", insert_loc(arr, x))
