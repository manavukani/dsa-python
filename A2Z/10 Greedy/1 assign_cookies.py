# g = greed factor
# s = size of cookies
# Find the maximum number of children you can satisfy (size >= greed) with the given cookies


def findContentChildren(g, s):
    g = sorted(g)
    s = sorted(s)

    count = 0
    i, j = 0, 0
    while i < len(g) and j < len(s):
        if g[i] <= s[j]:
            count += 1
            i += 1
            j += 1
        else:
            j += 1

    return count