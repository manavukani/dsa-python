class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        curr = 0
        for n in gain:
            curr += n
            highest = max(highest, curr)
        return highest