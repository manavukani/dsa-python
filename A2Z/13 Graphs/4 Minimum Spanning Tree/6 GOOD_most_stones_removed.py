# input - list of coordinates of stones placed on a grid, can remove a stone if there is another in same row/column
# output - most stones that can be removed


# INTUTION:
# - we can connect stones on same column/row and for a graph
# - for each component, we can remove: sub ans = vertices - 1
# - answer = total stones - # components = n - components
# - since we will minus 1 for each components, total verticces are n


# APPROACH!!! =====> Treat row and column as nodes
            # =====> if 0-4 rows, columns will be 5 onwards, ie: "col + max(rows) + 1" = 0 + 4 + 1 = 5


def removeMost(stones):
    maxRow = max(stone[0] for stone in stones)
    maxCol = max(stone[1] for stone in stones)

    # Total number of nodes (rows + columns as nodes)
    n = maxRow + maxCol + 2

    # Disjoint Set Union (DSU) logic
    par = [i for i in range(n)]
    rank = [1] * n

    def find(node):
        if node == par[node]:
            return node
        par[node] = find(par[node])
        return par[node]

    def union(node1, node2):
        p1 = find(node1)
        p2 = find(node2)

        if p1 != p2:
            if rank[p1] > rank[p2]:
                par[p2] = p1
            elif rank[p1] < rank[p2]:
                par[p1] = p2
            else:
                par[p2] = p1
                rank[p1] += 1

    # Union all stones
    for r, c in stones:
        union(r, c + maxRow + 1)

    # count connected components - find unique roots (row + column nodes)
    row_roots = {find(r) for r, c in stones}
    col_roots = {find(c + maxRow + 1) for r, c in stones}
    unique_components = row_roots | col_roots

    # total stones - number of components
    return len(stones) - len(unique_components)


stones = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]  # 5
print(removeMost(stones))
