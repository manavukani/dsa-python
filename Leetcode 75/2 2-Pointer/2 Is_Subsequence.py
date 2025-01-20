class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True

        s1 = 0
        s2 = 0

        while s1 < len(s) and s2 < len(t):
            if s[s1] == t[s2]:
                s1 += 1
                s2 += 1
            else:
                s2 += 1

        return s1 == len(s)
