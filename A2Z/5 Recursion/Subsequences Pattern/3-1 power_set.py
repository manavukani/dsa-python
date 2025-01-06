"""
APPROACH:
- The power set of a set is the set of all its subsets.
- The number of subsets of a set with n elements is 2^n.
- We iterate over all numbers from 0 to 2^n - 1 and for each number, we generate the corresponding subset.

- for say 3rd iteration, 3 in binary is 011
- so, we pick 0th and 1st element from the input array

BITWISE OPERATORS:
- 1 << n = 2^n
- i & (1 << j) = check if jth bit is set in i

TIME COMPLEXITY: O(2^n * n)
- for each number from 0 to 2^n - 1, we generate the corresponding subset
- for each number, we iterate over all bits in the number

SPACE COMPLEXITY: O(n)

"""


# NON RECURSIVE SOLUTION for all subsequences
# "power set" using binary representation
def power_set(arr):
    n = len(arr)

    # 0 to 2^n - 1 iterations
    for i in range(1 << n):
        subset = []

        # for each digit at each iteration
        # pick the set bits
        for j in range(n):
            if i & (1 << j):
                subset.append(arr[j])

        print(subset)


print("\nPOWER SET - NOT RECURSIVE")
arr = [3, 1, 2]
power_set(arr)
