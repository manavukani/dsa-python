# s = string
# k = number of replacements allowed

# eg: s = "AABABBA", k = 1
# output = 4

from collections import defaultdict
def characterReplacement(s: str, k: int) -> int:
    count = defaultdict(int)
    L = 0
    max_freq = 0
    # O(n)
    for R in range(len(s)):
        # add count of new ele
        count[s[R]] += 1

        max_freq = max(max_freq, count[s[R]])

        # CASE 1
        # if windowSize - mostFrequent <= k its doable to replace rest of char
        # so we increment R pointer (make window bigger)

        # CASE 2
        # if not we shrink the window (increment L pointer)
        if (R - L + 1) - max_freq > k:
            # rwmove the left most ele from window
            count[s[L]] -= 1
            L += 1

            # else case 1 is done auomatically -> increment R

    return R - L + 1
