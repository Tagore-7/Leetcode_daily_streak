class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_value, ans, curr_streak = 0,0,0
        for num in nums:
            if max_value < num:
                max_value = num
                ans, curr_streak = 0, 0
            if max_value == num:
                curr_streak += 1
            if max_value != num:
                curr_streak  = 0
            ans = max(ans, curr_streak)
        return ans
