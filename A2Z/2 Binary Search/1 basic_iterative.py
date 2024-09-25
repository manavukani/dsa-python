# If a number n can be divided by 2 for x times:
# 	2^x = n
# Therefore, x = log n (base is 2)

def binary_search(arr, target):
    low = 0
    high = len(arr)-1

    while low <= high:
        # mid = (low+high)//2
        mid = low + (high-low)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


if __name__ == "__main__":
    a = [3, 4, 6, 7, 9, 12, 16, 17]
    target = 6
    ind = binary_search(a, target)
    if ind == -1:
        print("The target is not present.")
    else:
        print("The target is at index:", ind)
