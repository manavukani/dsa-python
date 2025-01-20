class Solution:
    def uniqueOccurrences(self, arr):
        occ = {} # val -> occurence

        for n in arr:
            occ[n] = 1 + occ.get(n, 0)
        
        # check if all occurences are unique
        return len(occ) == len(set(occ.values()))
