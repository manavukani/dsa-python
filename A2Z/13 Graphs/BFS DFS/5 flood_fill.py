"""
- Start from sr,sc
- Mark all "connected" cells with the same color as (sr, sc) with the new color.
- Stop when no more adjacent pixels of the original color to update

"""


def flood_fill(image, sr, sc, color):
    if not image or not image[0]:
        return

    m, n = len(image), len(image[0])
    visited = set()

    starting_color = image[sr][sc]

    def dfs(r, c):
        # out of bounds or not same color or already visited
        if (
            r < 0
            or r >= m
            or c < 0
            or c >= n
            or image[r][c] != starting_color
            or (r, c) in visited
        ):
            return

        # mark as visited
        visited.add((r, c))

        # change color
        image[r][c] = color

        # explore all directions
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    dfs(sr, sc)
    return image


# test
image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1
color = 2
print(flood_fill(image, sr, sc, color))
