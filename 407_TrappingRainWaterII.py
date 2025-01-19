#Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.
#
# 
#
#Example 1:
#
#
#Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
#Output: 4
#Explanation: After the rain, water is trapped between the blocks.
#We have two small ponds 1 and 3 units trapped.
#The total volume of water trapped is 4.
#Example 2:
#
#
#Input: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
#Output: 10
# 
#
#Constraints:
#
#m == heightMap.length
#n == heightMap[i].length
#1 <= m, n <= 200
#0 <= heightMap[i][j] <= 2 * 104
#
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        ROWS, COLS = len(heightMap), len(heightMap[0])

        min_heap = []
        for r in range(ROWS):
            for c in range(COLS):
                if r in [0, ROWS -1 ] or c in [0, COLS -1]:
                    heappush(min_heap, (heightMap[r][c], r, c))
                    heightMap[r][c] = -1
        
        res = 0
        max_h = -1
        while min_heap:
            h, r, c = heappop(min_heap)
            max_h = max(max_h, h)
            res += max_h - h 

            neigh = [[r  + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
            for nr, nc in neigh:
                if ( nr < 0 or nc < 0 or nr == ROWS or nc == COLS or heightMap[nr][nc] == -1):
                    continue 

                heappush(min_heap, (heightMap[nr][nc], nr, nc))
                heightMap[nr][nc] = -1 
        
        return res

