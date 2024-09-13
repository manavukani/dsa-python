# Given an integer N and an array of size N-1 containing N-1 numbers between 1 to N.
# Find the number(between 1 to N), that is not present in the given array.

'''
array will be of length n
sum of n numbers - sum of array = remaining number

'''


def solve(nums):
    n = len(nums)
    sum_ideal = n*(n+1)//2
    # print(n, sum_ideal)
    for i in nums:
        sum_ideal -= i
    return sum_ideal


# result = solve([9, 6, 4, 2, 3, 5, 7, 0, 1])
# print(result)


'''
Property 1 => XOR of two same numbers is always 0 i.e. a ^ a = 0
Property 2 => XOR of a number with 0 will result in the number itself i.e. 0 ^ a = a

Assume the given array is: {1, 2, 4, 5} and N = 5.

XOR of (1 to 5) i.e. xor1 = (1^2^3^4^5)
XOR of array elements i.e. xor2 = (1^2^4^5)
XOR of xor1 and xor2 = (1^2^3^4^5) ^ (1^2^4^5)
			= (1^1)^(2^2)^(3)^(4^4)^(5^5)
			= 0^0^3^0^0 = 0^3 = 3.
The missing number is 3.
'''


def using_xor(nums):
    xor1 = 0
    xor2 = 0
    
    n = len(nums)

    # XOR all elements in the given array
    for num in nums:
        xor2 ^= num

    # XOR all numbers from 0 to N, inclusive both
    for i in range(n + 1):
        xor1 ^= i

    return xor1 ^ xor2


# Example usage
print(using_xor([9, 6, 4, 2, 3, 5, 7, 0, 1]))  # Output should be 8
