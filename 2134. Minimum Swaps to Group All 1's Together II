class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        total_ones_count = nums.count(1)
        ones_windows = max_window = 0
        N = len(nums)
        left = 0
        for right in range(2 * N):
            if(nums[right % N]):
                ones_windows += 1
            if right - left + 1 > total_ones_count:
                ones_windows -= nums[left % N]
                left += 1
            max_window = max(max_window, ones_windows)
        return total_ones_count - max_window
