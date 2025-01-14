# input = numCourses = 4, prerequisites = [[0,1],[3,2],[1,3],[0,3]]
# [ai, bi] indicates that you must take course bi first if you want to take course ai
# output = possible or not

from collections import deque


# Intution:
#   - if cyclic dependency, NOT possible
#   - view prereq as directed graph b -> a
# BFS vs DFS --- can do this with both but follow up needs BFS


def course_schedule_1(numCourses, prerequisites):
    # build adj
    adj = [[] for _ in range(numCourses)]
    for a, b in prerequisites:
        adj[b].append(a)

    # detect loop
    indegree = [0] * numCourses
    for i in range(numCourses):
        for nei in adj[i]:
            indegree[nei] += 1

    q = deque()
    for i in range(numCourses):
        if indegree[i] == 0:
            q.append(i)

    sizeOfTopo = 0
    while q:
        node = q.popleft()
        sizeOfTopo += 1

        for nei in adj[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)

    # same size -> no cycle -> possible | (size < V) -> cycle -> not possible
    return sizeOfTopo == numCourses


print(course_schedule_1(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))

"""
TC: O(V+E) ----> V = nodes and E = edges (simple BFS)

SC: O(2N) -----> N for indegree, N for queue
"""


# FOLLOW UP --- print the order of execution, given its possible
# RETURN TOPOLOGICAL SORTED ORDER ---> use array instead of just count
def course_schedule_2(numCourses, prerequisites):

    # build adj
    adj = [[] for _ in range(numCourses)]
    for a, b in prerequisites:
        adj[b].append(a)

    # detect loop
    indegree = [0] * numCourses
    for i in range(numCourses):
        for nei in adj[i]:
            indegree[nei] += 1

    q = deque()
    for i in range(numCourses):
        if indegree[i] == 0:
            q.append(i)

    # use topo sort
    topo = []

    while q:
        node = q.popleft()
        topo.append(node)

        for nei in adj[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)

    # same size -> no cycle -> possible
    if len(topo) == numCourses:
        return topo
    else:
        return []


print(course_schedule_2(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))

"""
TC: O(V+E) ----> V = nodes and E = edges (simple BFS)

SC: O(3N) -----> N for indegree, N for queue + O(N) for storing the topological sorting
"""
