'''
- You are given two strings s1 and s2.
- Return true if s2 contains a permutation of s1, or false otherwise.

- That means if permutation of s1 exists as a substring of s2, then return true.
- Both strings only contain lowercase letters.

Eg1:
Input: s1 = "abc", s2 = "lecabee"
Output: true

Eg2:
Input: s1 = "abc", s2 = "lecaabee"
Output: false
'''

# M1
# bruce force approach
# for each substring of s2, check if it is anagram of s1
# TC = O(n^3 * logn)

# M2
# hash map approach
# TC = O(n*m) where n is len(s1) and m is len(s2)
# use 2 maps, store freq, compare if they are equal at each step
def solve(s1, s2):
    count1 = {}
    for c in s1:
        count1[c] = 1 + count1.get(c, 0)

    need = len(count1)
    for i in range(len(s2)):
        count2, cur = {}, 0
        for j in range(i, len(s2)):
            count2[s2[j]] = 1 + count2.get(s2[j], 0)
            if count1.get(s2[j], 0) < count2[s2[j]]:
                break
            if count1.get(s2[j], 0) == count2[s2[j]]:
                cur += 1
            if cur == need:
                return True
    return False

'''
METHOD 3: Sliding window approach

s1 = "abc", s2 = "baxyzabc"

window size = 3 = len(s1)

s1count = [1, 1, 1, 0, 0, 0 ...... 0]
           a  b  c  d  e  f        z

for s2[0:3] = "bax"

s2count = [1, 1, 0, 0, 0, 0 ...... 1, 0, 0]
           a  b  c  d  e  f        x  y  z

match(s1, s2[0:3]) = 24 (c and x are not matching)


- we match s1count and s2count, 
- if we get 26 matches, we return True
- else we move the window to right by 1 and update the s2count
    - decrease the count of s2[l] by 1
    - increase the count of s2[r] by 1
- if reach end of s2, check for last window, else return False

'''

# M3- slinding window approach
# TC = O(n) where n is len(s2)
def checkInclusion(s1, s2):
    if len(s1) > len(s2):
        return False

    # initialize with 0
    s1Count, s2Count = [0] * 26, [0] * 26
    
    # count the freq of each char for window size (len(s1))
    for i in range(len(s1)):
        s1Count[ord(s1[i]) - ord('a')] += 1
        s2Count[ord(s2[i]) - ord('a')] += 1

    # compare s1Count and s2Count
    matches = 0
    for i in range(26):
        matches += (1 if s1Count[i] == s2Count[i] else 0)

    # for each next window
    # update the s2Count
    # check if matches == 26 => return True 
    l = 0
    for r in range(len(s1), len(s2)):
        if matches == 26:
            return True

        # increment the new char count
        index = ord(s2[r]) - ord('a')
        s2Count[index] += 1
        # check if s1Count and s2Count equal @ idx  => increment matches
        if s1Count[index] == s2Count[index]:
            matches += 1
        elif s1Count[index] + 1 == s2Count[index]:
            matches -= 1

        # decrement the old char count
        index = ord(s2[l]) - ord('a')
        s2Count[index] -= 1
        # check if s1Count and s2Count equal @ idx  => increment matches
        if s1Count[index] == s2Count[index]:
            matches += 1
        elif s1Count[index] - 1 == s2Count[index]:
            matches -= 1
        
        # move the window to right
        l += 1
    
    # check for last window
    return matches == 26
