class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        
        def check_magic_square(matrix):
            num_list = defaultdict(int)
            first_diag_sum = 0
            reverse_diag_sum = 0
            n = len(matrix)
            for i in range(n):
                row_sum = sum(matrix[i])
                col_sum = sum(matrix[j][i] for j in range(n))

                if row_sum != col_sum:
                    return False

                for j in range(n):
                    num_list[matrix[i][j]] += 1
                    if i == j :
                        first_diag_sum += matrix[i][j]
                    if i + j == n - 1:
                        reverse_diag_sum += matrix[i][j]      
            for key, value in num_list.items():
                if value > 1 or key < 1 or key > 9:
                    return False

            if reverse_diag_sum != first_diag_sum:
                return False

            return first_diag_sum ==  col_sum

        res = 0
        for i in range(len(grid) - 2 ):
            for j in range(len(grid[0]) - 2):
                matrix = [row[j:j +3] for row in grid[i:i + 3]]
                if check_magic_square(matrix):
                    res += 1
        return res
            
        
