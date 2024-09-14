class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        directions = [[0, 1], [1, 0],[0, -1], [-1, 0]]
        i = 0
        steps = 1
        res = []
        curr_row, curr_col = rStart, cStart
        while len(res) < rows * cols:
            for x in range(2):
                r, c = directions[i]
                for y in range(steps):
                    if 0 <= curr_row < rows and 0 <= curr_col < cols:
                        res.append([curr_row, curr_col])
                    curr_row, curr_col = curr_row + r, curr_col + c
                i = (i + 1) % 4
            steps += 1
        return res
