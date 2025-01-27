# TC = O(N logN)
class Solution:
    def successfulPairs(self, spells, potions, success):
        ans = []
        potions.sort()  # O(N logN)
        for sp in spells:  # O(N)
            l = 0
            h = len(potions)
            while l < h:  # O(log N)
                mid = (l + h) // 2
                if sp * potions[mid] >= success:
                    h = mid
                else:
                    l = mid + 1

            ans.append(len(potions) - l)
        return ans


# uses concept similar to bisect left in python (refer A2Z/Binary Search -> 3 lower_bound, 4 upper_bound)
# bisect_left returns idx of smallest ele >= x
from bisect import bisect_left


def solveWithBisect(spells, potions, success):
    ans = []
    potions.sort()
    for sp in spells:
        po = (success + sp - 1) // sp
        threshold_idx = bisect_left(potions, po)
        ans.append(len(potions) - threshold_idx)
    return ans


"""
spell * potion >= success
potion >= ceil(success/spell)
potion >= (success + spell - 1) / spell ------> to avoid precision error
# ensures proper rounding up to the next integer when dividing integers
"""
