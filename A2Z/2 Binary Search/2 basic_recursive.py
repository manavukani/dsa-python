# The base case of the recursion will be low > high. If (low > high),
# the search space becomes invalid which means the target is not present in the array.

# not a problem in python, but for c/c++
# mid = low + (high-low)//2

def binary_search(arr, low, high, target):
    mid = low + (high-low)//2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, low, mid-1, target)
    else:
        return binary_search(arr, mid+1, high, target)


if __name__ == "__main__":
    a = [3, 4, 6, 7, 9, 12, 16, 17]
    target = 6
    ind = binary_search(arr=a, low=0, high=(len(a)-1), target=target)
    if ind == -1:
        print("The target is not present.")
    else:
        print("The target is at index:", ind)
