class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res = 0
        n = len(rating)
        for middle in range(1, n):
            left_small_numbers = right_larger_numbers = 0
            for i in range(middle):
                if rating[i] < rating[middle]:
                    left_small_numbers += 1
            for i in range(middle+1, n):
                if rating[i] > rating[middle]:
                    right_larger_numbers += 1
            res += left_small_numbers * right_larger_numbers
            left_largers_numbers = middle - left_small_numbers
            right_small_numbers = len(rating) - 1 - middle - right_larger_numbers
            res += left_largers_numbers * right_small_numbers
        return res
