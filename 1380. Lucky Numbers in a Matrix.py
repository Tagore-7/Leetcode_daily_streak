class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        lucky_numbers = []

        for i in range(len(matrix)):
            min_value = min(matrix[i])

            for j in range(len(matrix[0])):
                max_value =  max(matrix[k][j] for k in range(len(matrix)))
                if matrix[i][j] == min_value and matrix[i][j] == max_value:
                    lucky_numbers.append(matrix[i][j])
        return lucky_numbers
