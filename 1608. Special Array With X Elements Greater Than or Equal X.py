class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        for i in range(len(nums)):
            # print(i)
            if nums[i] >= i +1:
                # print(nums[i])
                if i == len(nums) - 1 or nums[i + 1] < i + 1:
                    # print(i)
                    return i + 1
                
        return -1
