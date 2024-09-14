class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c, visit):
            if 0 > r or r == ROWS or 0 > c or c == COLS or (r,c) in visit or grid[r][c] == 0:
                return 
            visit.add((r, c))
            neighbours = [[r, c + 1], [r + 1, c], [r, c- 1], [r -1 , c]]
            for nr, nc in neighbours:
                dfs(nr, nc, visit)

        def count_islands():
            visit = set()
            count = 0
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c]  and (r,c) not in visit:
                        dfs(r, c, visit)
                        count += 1
            return count 

        if count_islands() != 1:
            return 0
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    continue
                grid[r][c] = 0
                if count_islands() != 1:
                    return 1
                grid[r][c] = 1
        return 2
        
