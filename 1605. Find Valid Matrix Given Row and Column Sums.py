class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n = len(rowSum)
        m = len(colSum)

        org_matrix = [[0] * m for _ in range(n)]

        # print(org_matrix)
        i, j = 0, 0

        while i < n and  j < m:
            org_matrix[i][j]  = min(rowSum[i], colSum[j])

            rowSum[i] -= org_matrix[i][j]
            colSum[j] -= org_matrix[i][j]

            if rowSum[i] == 0:
                i += 1
            else:
                j += 1  
        return org_matrix
