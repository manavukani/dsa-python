from collections import defaultdict
from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        # occ1 = defaultdict(int)
        # for c in word1:
        #     occ1[c] += 1
        
        # occ2 = defaultdict(int)
        # for c in word2:
        #     occ2[c] += 1
        
        occ1 = Counter(word1)
        occ2 = Counter(word2)
        
        # for operation 1, need same freq count (can swap posn), cant use hashset - eliminate duplicates
        if sorted(occ1.values()) != sorted(occ2.values()):
            return False
        
        # for operation 2, both must have same chars
        if set(occ1.keys()) != set(occ2.keys()):
            return False
        
        # passes all checks
        return True
        

word1 ="cabbba"
word2 ="abbccc"

print(Solution().closeStrings(word1, word2))