# Matrix (2D grid)

grid = [[0,0,0,0],
        [1,1,0,0],
        [0,0,0,1],
        [0,1,0,0]]

# count paths (backtracking)
ROWS, COLS = len(grid), len(grid[0])

def dfs(r, c, visit):
    if min(r, c) < ROWS or r == ROWS or c == COLS or (r, c) in visit or grid[r][c] == 1:
        return 0
    if r == ROWS - 1 and c == COLS - 1:
        return 1

    visit.add((r, c))

    count = 0
    count += dfs( r + 1, c, visit)
    count += dfs( r - 1, c, visit)
    count += dfs(r, c - 1, visit)
    count += dfs(r, c + 1, visit)
    
    visit.remove((r, c))

    return count 

return dfs(0,0, set())

