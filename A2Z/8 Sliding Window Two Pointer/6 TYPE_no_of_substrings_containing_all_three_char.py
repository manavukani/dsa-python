# input: s = bbacba
# output: # substrings with all 3 char
from collections import defaultdict

# O(n^2)


def brute(s):
    cnt = 0
    for i in range(len(s)):
        mpp = defaultdict(int)
        for j in range(i, len(s)):
            # exist -> true
            mpp[s[j]] = 1
            if mpp['a'] + mpp['b'] + mpp['c'] == 3:
                # cnt += 1
                cnt += (len(s)-j)
                # small optimization - all the following substring will be valid no need to traverse
                break
    return cnt


'''
with every char there is a substring that ends
traverse reverse for each char

s = bbacba
        ^
        |
for this b -> minimum window = acb
other substrings are bbacb, bacb


METHOD:
- we traverse from left and maintain last seen for a, b and c
- as soon as we have all 3
- we check elements on left, say 2 ---> no. of valid substrings = 1 + (2) = 3
- we move ahead and again update last seen
- and again check elements on left and repeat...

'''
# O(N)
def optimal(s):
    lastseen = [-1, -1, -1]
    cnt = 0
    for i in range(len(s)):
        lastseen[ord(s[i]) - ord('a')] = i
        # can also omit this if condition, coz if not exist min(a,b,c) = -1 and 1 + (-1) = 0
        # so count wont be incremented
        if lastseen[0] != -1 and lastseen[2] != -1 and lastseen[2] != -1:
            cnt = cnt + 1 + min(lastseen[0], lastseen[1], lastseen[2])
    return cnt

print(optimal('bbacba'))
