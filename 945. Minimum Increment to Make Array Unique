class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()
        next_unique = nums[0]
        count = 0

        for num in nums:
            if num < next_unique:
                count += next_unique - num
                next_unique += 1
            else:
                next_unique = num + 1
        return count
