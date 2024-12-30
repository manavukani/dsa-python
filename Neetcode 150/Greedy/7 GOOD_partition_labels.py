# split the string such that each char is in 1 paratition only
# return the list of sizes of partition

"""

i/p - ababcbaca | defegde | hijhklij

o/p = [9,7,8]

- for each char we want to know its last posn so we can split.
- but need to check if any char within that range is outside it or not 

Approach:
- find last idx for all char
- traverse through string
    - increment size
    - check if last idx for current ele > current end, if so update --- max
    - if we reach end, that means we have complete 1 partition, append size to res and reset size 

"""


# O(N)
def partitionLabels(s):
    # find the last index for all char
    lastIndex = {}
    for i, c in enumerate(s):
        lastIndex[c] = i

    res = []
    size = end = 0
    for i, c in enumerate(s):
        size += 1
        # update the end for each char
        end = max(end, lastIndex[c])

        if i == end:
            res.append(size)
            size = 0
    return res
