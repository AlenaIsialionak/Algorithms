import typing
from collections import deque

def numIslands(grid: typing.List[str]) -> int:
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visit = set()
    islands = 0

    def bfs(r, c):
        q = deque()
        visit.add((r, c))
        q.append((r, c))

        while q:
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            row, col = q.popleft()
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if (r in range(rows)) and (c in range(cols)) and grid[r][c] == '1' and (r, c) not in visit:
                    visit.add((r, c))
                    q.append((r, c))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r, c) not in visit:
                bfs(r, c)
                islands += 1

    return islands


grid = [
    ["1", "1", "1"],
    ["0", "1", "0"],
    ["1", "1", "1"]
]
a = numIslands(grid)
print(a)