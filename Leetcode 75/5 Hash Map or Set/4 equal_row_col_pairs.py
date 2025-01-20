from collections import defaultdict


class Solution:
    def equalPairs(self, grid) -> int:
        master = defaultdict(int)
        equal_pairs_count = 0
        n = len(grid)

        # count frequency of rows
        for i in range(n):
            master[tuple(grid[i])] += 1

        # count frequency of columns
        for i in range(n):
            col = []
            for j in range(len(grid[0])):
                col.append(grid[j][i])
            col = tuple(col)

            # if column tuple is in master, add to count
            if master[col]:
                equal_pairs_count += master[col]

        return equal_pairs_count


print(Solution().equalPairs([[3, 2, 1], [1, 7, 6], [2, 7, 7]]))  # 1
print(Solution().equalPairs([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]))  # 3
