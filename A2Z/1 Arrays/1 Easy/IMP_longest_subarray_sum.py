'''
Example 1:
Input Format: N = 3, k = 5, array[] = {2,3,5}
Result: 2
Explanation: The longest subarray with sum 5 is {2, 3}. And its length is 2.

Example 2:
Input Format: N = 5, k = 10, array[] = {2,3,5,1,9}
Result: 3
Explanation: The longest subarray with sum 10 is {2, 3, 5}. And its length is 3.

'''

# silly brute force - find all sub arrays
# O (n^3)


def brute_force(arr, k):
    n = len(arr)  # size of the array.

    length = 0
    for i in range(n):  # starting index
        for j in range(i, n):  # ending index
            # add all the elements of subarray = a[i...j]:
            s = 0
            for _ in range(i, j+1):
                s += arr[_]

            if s == k:
                length = max(length, j - i + 1)
    return length

# naive approach - brute force
# instead of using for loop to sum the array
# we add just the new element
# O (n^2)


def brute_n2(arr, k):
    n = len(arr)

    length = 0
    for i in range(n):
        s = 0
        for j in range(i, n):
            # add new element
            s += arr[j]

            if s == k:
                length = max(length, j-i+1)
    return length


# better approach --------- BEST IF HAS BOTH POSITIVE AND NEGATIVE
# hashing
# works but edge case, cannot handle zero => check video - https://youtu.be/frf7qxiN2qU
'''
TIME COMPLEXITY: O(N) or O(N*logN) depending on which map data structure we are using, where N = size of the array.

REASON: For example, if we are using an unordered_map data structure in C++ the time complexity will be O(N)(though in the worst case, unordered_map takes O(N) to find an element and the time complexity becomes O(N2)) but if we are using a map data structure, the time complexity will be O(N*logN). The least complexity will be O(N) as we are using a loop to traverse the array.

'''


def better(arr, k):
    pre_sum = {}  # prefix sum map
    s = 0  # sum
    max_length = 0

    for i in range(len(arr)):
        s += arr[i]

        if (s == k):
            max_length = max(max_length, i+1)
        remain = s - k

        if remain in pre_sum:
            length = i - pre_sum[remain]
            max_length = max(length, max_length)

        # only update if DNE
        if s not in pre_sum:
            pre_sum[s] = i
    return max_length

# ----------- OPTIMAL --------- BEST IF ONLY POSITIVES & ZERO
# 2 pointers


def optimal(arr, k):
    left, right = 0, 0
    s = arr[0]  # sum
    max_length = 0
    n = len(arr)
    while (right < n):
        # if sub array exist and sum exceeds k
        while left <= right and s > k:
            s -= arr[left]  # exclude left element
            left += 1  # shrink
        # if equal check the max length
        if s == k:
            max_length = max(max_length, right-left+1)
        right += 1
        if right < n:  # prevent out of index
            s += arr[right]
    return max_length


if __name__ == "__main__":
    arr = [2, 3, 5, 1, 9]
    k = 10
    
    # print(brute_force(arr, k))
    # print(brute_n2(arr, k))
    print(optimal(arr, k))


    # arr = [-1, 1, 1]
    # k = 1
    
    # print(better(arr, k))