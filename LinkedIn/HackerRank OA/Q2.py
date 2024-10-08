# Similar Numbers

'''
Two numbers, without leading zeros, are similar if rearranging the digits gives matching numbers, i.e., numbers with the equal frequency of each digit. For example, the numbers 1100 and 1001 are similar, but 1100 and 0110 are not similar because 0110 has a leading zero.

Given two strings that represent long integers a and b, check their similarity. 

Based on the finding, determine one of the following:
=> If a and bare similar, find the total number of similar numbers to a.
=> If a and bare not similar, find the total number of similar numbers to b.

Ex:

a=112, b=121 => numbers similar to a: 112, 121, 211
a=11, b=223  => numbers similar to b: 223, 232, 322
'''

from math import factorial
from collections import Counter

def findSimilar(a: str, b: str) -> int:

    def are_similar(a: str, b: str) -> bool:
        return Counter(a) == Counter(b)

    def count_unique_permutations(s: str) -> int:
        n = len(s)
        counts = Counter(s)

        # Calculate total unique permutations
        total = factorial(n)
        for count in counts.values():
            total //= factorial(count)

        # If '0' is present and the number has more than one digit, subtract permutations with leading '0'
        if '0' in counts and counts['0'] > 0 and n > 1:
            counts_zero_first = counts.copy()
            counts_zero_first['0'] -= 1  # Fix '0' as the first digit

            # Calculate permutations for the remaining digits
            zero_first = factorial(n - 1)
            for count in counts_zero_first.values():
                zero_first //= factorial(count)

            total_valid = total - zero_first
            return total_valid
        else:
            return total

    # Determine similarity
    similar = are_similar(a, b)

    # Count based on similarity
    if similar:
        return count_unique_permutations(a)
    else:
        return count_unique_permutations(b)

test = [[1234, 2341], [1100, 1001], [1234, 1213]]  # 24, 3, 12

for i in test:
    print(findSimilar(str(i[0]), str(i[1])))
    print()
