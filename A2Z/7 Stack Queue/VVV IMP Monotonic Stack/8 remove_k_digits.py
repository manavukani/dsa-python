"""
INPUT => string num (non-negative integer), and an integer k 
OUTPUT => smallest possible integer after removing k digits from num

Eg1:
K = 3
1 4 3 2 2 1 9
"""

# keep smaller digits at start -> traverse from start
# remove larger ones

# keep adding to stack until find a smaller element -> traversing in increasing order
# remove the top from string (largest till now), decrement k
# when find equal push

# EDGE CASES:
# k == n? -> remove everything -> return "0"
# invalid numbers? "00001" -> trim starting zeroes
# if increasing order (eg: [1 2 3 4 5 6], k = 3) -> k not 0 at end, remove last k


def removeKdigits(num, k):
    stack = []
    for digit in num:
        # Key logic: remove larger digits to keep number smaller
        while k > 0 and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    # CASE 3
    # If we still need to remove digits after iteration
    # Remove from the end (largest digits)
    while k > 0:
        stack.pop()
        k -= 1
    # CASE 2
    result = "".join(stack).lstrip("0")
    # CASE 1
    return result if result else "0"

