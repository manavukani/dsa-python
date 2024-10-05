# O(NlogN)
def with_sorting(arr):
    n = len(arr)
    if n == 0 or n == 1:
        print(-1, -1)  # edge case when only one element is present in array
    arr.sort()
    small = arr[1]
    large = arr[-2]
    print("Second smallest is", small)
    print("Second largest is", large)

# Find the smallest and largest
# again traverse and find just greater than the smallest element
# O(N), double pass
def brute_force(arr):
    n = len(arr)
    if n == 0 or n == 1:
        print(-1, -1)
    small = float('inf')
    second_small = float('inf')
    large = float('-inf')
    second_large = float('-inf')

    for i in range(n):
        small = min(small, arr[i])
        large = max(large, arr[i])

    for i in range(n):
        if arr[i] < second_small and arr[i] != small:
            second_small = arr[i]
        if arr[i] > second_large and arr[i] != large:
            second_large = arr[i]

    print("Second smallest is", second_small)
    print("Second largest is", second_large)

# traverse and keep track simultaneously
# larger than 'large' => update second_large and large
# is larger than only 'second_large' => update second_large
# O(N), single pass
def optimal(arr):

    n = len(arr)

    def secondSmallest(arr, n):
        if (n < 2):
            return -1
        small = float('inf')
        second_small = float('inf')
        for i in range(n):
            if (arr[i] < small):
                second_small = small
                small = arr[i]
            elif (arr[i] < second_small and arr[i] != small):
                second_small = arr[i]
        return second_small

    def secondLargest(arr, n):
        if (n < 2):
            return -1
        large = float('-inf')
        second_large = float('-inf')
        for i in range(n):
            if (arr[i] > large):
                second_large = large
                large = arr[i]
            elif (arr[i] > second_large and arr[i] != large):
                second_large = arr[i]
        return second_large

    return secondLargest(arr, n), secondSmallest(arr, n)


arr = [1, 2, 4, 7, 7, 5]
sL, sS = optimal(arr)
print("Second smallest is", sS)
print("Second largest is", sL)
