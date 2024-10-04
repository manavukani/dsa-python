# Print all the elements which are leaders
# A Leader is an element that is greater than (equal to) all of the elements
# on its right side in the array.

# [4, 7, 1, 0] ==> 7 1 0
# [10, 22, 12, 3, 0, 6] ==> 22, 12, 6

# BRUTE => for each element check on right if any is greater
#       => if not then append, else move to next

def optimal(nums):
    stack = []
    # start from back of array
    for i in range(len(nums)-1, -1, -1):
        # if top of stack is less than equal to current num, means
        if not stack or nums[i] >= stack[-1]:
            stack.append(nums[i])
    stack.reverse()
    return stack

print(optimal([10, 22, 12, 3, 0, 6]))
print(optimal([5,4,3]))
print(optimal([16, 17, 4, 3, 5, 2]))
print(optimal([31, 40, 93, 40, 98]))


# STACK NOT ALLOWED. use max element variable
# def printLeaders(arr, n):
#     ans = []
#     max_elem = arr[n - 1]
#     ans.append(arr[n - 1])
#     for i in range(n - 2, -1, -1):
#         if arr[i] > max_elem:
#             ans.append(arr[i])
#             max_elem = arr[i]
#     return ans