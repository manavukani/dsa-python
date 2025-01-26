# rooms = [[1],[2],[3],[]]
# # rooms = [[1,3],[3,0,1],[2],[0]]


def canVisitAllRooms(rooms):
    # rooms = adj list
    visited = [False] * len(rooms)
    visited[0] = True

    def dfs(room):
        visited[room] = True
        for key in rooms[room]:
            if not visited[key]:
                dfs(key)

    dfs(0)

    if False in visited:
        return False

    return True


# with stack, iterative
def usingStack(rooms):
    visited = set()
    stack = []

    stack.append(0)

    while stack:
        curr = stack.pop()
        visited.add(curr)
        for nei in rooms[curr]:
            if nei not in visited:
                stack.append(nei)

    return len(visited) == len(rooms)
