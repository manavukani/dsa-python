class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        curr = 0
        maxAns = 0

        l = 0
        r = 0

        # initial window
        while r < k:
            if s[r] in vowels:
                curr+=1
            r+=1
        
        maxAns = curr

        # r @ kth index till ---> n-1
        while r < len(s):
            if s[l] in vowels:
                curr -= 1
            if s[r] in vowels:
                curr += 1
            maxAns = max(curr, maxAns)
            l+=1
            r+=1
        
        return maxAns

            