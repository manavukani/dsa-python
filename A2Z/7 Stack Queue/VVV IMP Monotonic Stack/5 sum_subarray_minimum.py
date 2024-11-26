'''
OUTPUT =>  arr = [3,1,2,4]
Explanation: Subarrays = [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1
OUTPUT => 17
'''

# brute -> generate all subarray, find min of each subarray, add to result
# O(n^3) -> O(n^2) for subarrays, O(n) for min of subarray


def brute(arr):
    n = len(arr)
    res = 0
    for i in range(n):
        for j in range(i, n):
            res += min(arr[i:j + 1])
    return res


'''
Eg1: arr = [3,1,2,4]

- no. of subarray where 3 is minimum = 1
- no. of subarray where 1 is minimum = 6
- no. of subarray where 2 is minimum = 2
- no. of subarray where 4 is minimum = 1

OUTPUT = 3*1 + 1*6 + 2*2 + 4*1 = 17

Eg2: arr = [1, 4, 6, 7, 3, 7, 8, 1]

Method:
1. Find the left and right boundary of each element -> Next smaller element to left and right
2. Find the no. of subarray which can be generated -> A * B =  (i - left) * (right - i)
3. Add no. of subarray * arr[i] to result

'''

# WORK IN PROGRESS

def previous_smaller_element(arr):
    stack = []
    res = []
    for ele in arr:
        while stack and stack[-1] >= ele:
            stack.pop()
        if stack:
            res.append(stack[-1])
        else:
            res.append(-1)
        stack.append(ele)
    return res


def next_smaller_element(arr):
    stack = []
    res = []
    for ele in arr[::-1]:
        while stack and stack[-1] >= ele:
            stack.pop()
        if stack:
            res.append(stack[-1])
        else:
            res.append(-1)
        stack.append(ele)
    return res[::-1]


def optimal(arr):
    nse = next_smaller_element(arr)
    pse = previous_smaller_element(arr)
    total = 0
    for i in range(len(arr)):
        print(i, arr[i], pse[i], nse[i])
        print((i - pse[i]) * (nse[i] - i))
        print("----")
        left = i - pse[i]
        right = nse[i] - i
        total += left * right * arr[i]

    return total


input = [3, 1, 2, 4]
print(optimal(input))
