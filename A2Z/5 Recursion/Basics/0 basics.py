""" ============ PARAMETER BASED RECURSION ============ 

accumulator-based recursion, this approach involves passing parameters to the recursive function to
keep track of the state of the recursion. The parameters are updated at each recursive call,
allowing the function to accumulate the results of the recursion

"""


# normal recursion
def Nto1(N):
    def helper(i, N):
        if i < 1:
            return
        print(i)
        helper(i - 1, N)

    helper(N, N)


# using backtracking
def Nto1(N):
    def helper(i, N):
        if i > N:
            return
        helper(i + 1, N)
        print(i)  # stuff happens when coming back from recursion

    helper(1, N)


# Nto1(4)


# SUM OF N NATURAL NUMBERS
def usingParameters(N):
    def helper(i, sum):
        if i < 1:
            print(sum)
            return
        helper(i - 1, sum + i)

    helper(N, 0)


usingParameters(10)


""" ============ FUNCTIONAL RECURSION ============ 

The function's parameters are used to control the flow of the recursion, and 
function "returns" a value based on these parameters

"""


def functionalRecursion(N):
    if N == 0:
        return 0
    return N + functionalRecursion(N - 1)


print(functionalRecursion(10))


# Factorial
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


print(factorial(5))

""" ============ REVERSE ARRAY ============ """


def using2Pointer(arr):
    def helper(l, r):
        if l >= r:
            return
        arr[l], arr[r] = arr[r], arr[l]
        helper(l + 1, r - 1)

    helper(0, len(arr) - 1)


arr = [1, 2, 3, 4, 5]
using2Pointer(arr)
print(arr)


# Single Pointer (also without helper function, just pass array with index)
def usingSinglePointer(arr, i):
    if i >= len(arr) // 2:
        return
    arr[i], arr[len(arr) - i - 1] = arr[len(arr) - i - 1], arr[i]
    usingSinglePointer(arr, i + 1)


usingSinglePointer(arr, 0)
print(arr)


""" ============ PALINDROME ============ """


# functional recursion - we return using recursion
def isPalindrome(s, index):
    # base case -- false not returned till end, so true
    if index >= len(s) // 2:
        return True
    if s[index] != s[len(s) - index - 1]:
        return False
    return isPalindrome(s, index + 1)


s = "racecar"
print(isPalindrome(s, 0))

""" ============ MULTIPLE RECURSIVE CALLS ============ """


# fibonacci
def fibonacci(n):
    # for n = 0 => 0 and n = 1 => 1
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(5))
