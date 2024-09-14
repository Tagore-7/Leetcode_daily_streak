class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_ind = {}
        n = len(nums)
        for i in range(n):
            num = target - nums[i]
            if num in num_ind:
                return [i, num_ind[num]]
            num_ind[nums[i]] = i 
        return -1

        

        
