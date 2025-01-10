# we use kahn's algo

# INTUTION:
#   - we know topo sort cannot be done for "directed cyclic graphs"
#   - but still we do
#   - topo sort will NOT be of N size due to cycle -- will be less than N
#   - hence we can say it has cycle


from collections import deque


def cycle_detection_BFS(adj):
    V = len(adj)
    indegree = [0] * V
    for i in range(V):
        for nei in adj[i]:
            indegree[nei] += 1

    q = deque()
    for i in range(V):
        if indegree[i] == 0:
            q.append(i)

    topoSortSize = 0  # save space by not saving topo sort, just size
    while q:
        node = q.popleft()

        topoSortSize += 1

        for nei in adj[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)

    if topoSortSize == V:
        return False
    else:
        return True

