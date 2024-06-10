class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ans = 0
        expected = sorted(heights)
        for i in range(len(heights)):
            if heights[i] != expected[i]:
               ans += 1

        return ans
